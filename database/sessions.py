from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.config import DATABASE_URL


# Create the engine with conect in DB
engine = create_engine(DATABASE_URL)

# Create the session
Local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base
Base = declarative_base()

def get_db ():
    db = Local_session()
    try:
        yield db
    finally:
        db.close()