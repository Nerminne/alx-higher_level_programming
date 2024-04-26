#!/usr/bin/python3
"""file that contains the class definition of a State"""


from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class State(Base):
    """
    Attributes:
        id -> int, unique, not nullable
        name ->  str, max char 128
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
