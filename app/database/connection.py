from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://jobtracker:jobtracker@localhost:5432/jobtracker"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)