from sqlalchemy import Column, Integer, String
from db import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    # User query
    query = Column(String, nullable=False)

    # Bot response
    response = Column(String, nullable=True)

    # Priority: low / medium / high
    priority = Column(String, nullable=False)

    # Status: open / resolved
    status = Column(String, default="open")