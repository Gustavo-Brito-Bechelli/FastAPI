from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todos(Base):
    __tableName__ = 'todos'     # todos == tarefas

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=True)
