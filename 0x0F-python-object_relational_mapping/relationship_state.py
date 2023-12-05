#!/usr/bin/python3
"""Create state class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import  Base


class State(Base):
    '''
    SQLAlchemy model representing a state.

    Attributes:
    - id: An auto-incrementing integer, the primary key.
    - name: A string representing the name of the state.
    - cities: A one-to-many relationship with the City class.
    '''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          cascade="all, delete-orphan",
                          backref="states")
