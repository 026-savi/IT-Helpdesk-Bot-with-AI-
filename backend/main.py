from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from agent import handle_query
from sentiment import detect_priority
from db import SessionLocal, create_tables
from models import Ticket

# 🔧 Create DB tables
create_tables()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# 📦 REQUEST MODELS
# -----------------------------

class ChatRequest(BaseModel):
    query: str


class TicketUpdate(BaseModel):
    status: str   # open / resolved / closed


# -----------------------------
# 🗄️ DATABASE DEPENDENCY
# -----------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# 🏠 HOME
# -----------------------------

@app.get("/")
def home():
    return {"message": "IT Helpdesk Bot Running 🚀"}


# -----------------------------
# 💬 CHAT API (AUTO TICKET)
# -----------------------------

@app.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):

    query = request.query

    # Get AI response
    response = handle_query(query)

    # Detect priority
    priority = detect_priority(query)

    # Auto decide status
    status = "resolved"

    if "No solution found" in response:
        status = "open"

    # Create ticket
    ticket = Ticket(
        query=query,
        response=response,
        priority=priority,
        status=status
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return {
        "response": response,
        "priority": priority.upper(),
        "ticket_id": ticket.id,
        "status": status.upper()
    }


# -----------------------------
# 📋 GET ALL TICKETS
# -----------------------------

@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()

    return [
        {
            "id": t.id,
            "query": t.query,
            "response": t.response,
            "status": t.status,
            "priority": t.priority
        }
        for t in tickets
    ]


# -----------------------------
# 🔍 GET SINGLE TICKET
# -----------------------------

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {
        "id": ticket.id,
        "query": ticket.query,
        "response": ticket.response,
        "status": ticket.status,
        "priority": ticket.priority
    }


# -----------------------------
# ✏️ UPDATE TICKET (ADMIN)
# -----------------------------

@app.patch("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, update: TicketUpdate, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    ticket.status = update.status
    db.commit()
    db.refresh(ticket)

    return {
        "message": "Ticket updated successfully",
        "ticket": {
            "id": ticket.id,
            "status": ticket.status
        }
    }


# -----------------------------
# 📊 DASHBOARD STATS
# -----------------------------

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Ticket).count()
    open_tickets = db.query(Ticket).filter(Ticket.status == "open").count()
    resolved = db.query(Ticket).filter(Ticket.status == "resolved").count()
    urgent = db.query(Ticket).filter(Ticket.priority == "high").count()

    return {
        "total": total,
        "open": open_tickets,
        "resolved": resolved,
        "urgent": urgent
    }
    
    
    
    # 🔥 DASHBOARD STATS API
@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):

    total = db.query(Ticket).count()

    open_tickets = db.query(Ticket).filter(
        Ticket.status == "open"
    ).count()

    resolved_tickets = db.query(Ticket).filter(
        Ticket.status == "resolved"
    ).count()

    high_priority = db.query(Ticket).filter(
        Ticket.priority == "high"
    ).count()

    return {
        "total_tickets": total,
        "open_tickets": open_tickets,
        "resolved_tickets": resolved_tickets,
        "high_priority_tickets": high_priority
    }
    
    # 🎫 GET ALL TICKETS API

@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):

    tickets = db.query(Ticket).all()

    return tickets