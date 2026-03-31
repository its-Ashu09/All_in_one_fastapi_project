from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

mysql_url = os.getenv("DATABASE_url")


engine = create_engine(mysql_url)

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)



Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
