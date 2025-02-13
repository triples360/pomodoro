from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql://postgres:postgres@localhost:5432/pomodoro")
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    remaining_time = Column(Integer)
    total_time = Column(Integer)
    focus_duration = Column(Integer)
    break_duration = Column(Integer)

Base.metadata.create_all(engine)
