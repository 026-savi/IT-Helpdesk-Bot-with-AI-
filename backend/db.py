from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite DB
DATABASE_URL = "sqlite:///./tickets.db"

# Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ SINGLE Base (used everywhere)
Base = declarative_base()


# 🔥 CREATE TABLES FUNCTION (IMPORTANT)

def create_tables():

    from backend import models

    Base.metadata.create_all(bind=engine)