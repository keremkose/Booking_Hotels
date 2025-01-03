from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL="sqlite:///./hotel_bookings.db"

engine= create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
 
Base = declarative_base()

metadata = MetaData()
metadata.reflect(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()