from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker, Session
Base = declarative_base()



class Task(Base):
    __tablename__ = "tasks"
    task_no= Column(Integer, primary_key=True, index=True)
    task_name= Column(String, index=True)
