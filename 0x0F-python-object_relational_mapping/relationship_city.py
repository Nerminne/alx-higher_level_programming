#!/usr/bin/python3
"""create city class"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Attributes:
        id -> int, not nullable, unique
        name -> str, max char 128
        state_id -> int, not nullable, from states table (State)
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
