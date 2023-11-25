#!/usr/bin/python3
'''define city class'''

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    '''
    SQLAlchemy model representing a city.

    Attributes:
    - id: An auto-incrementing integer, the primary key.
    - name: A string representing the name of the city.
    - state_id: An integer representing the foreign key
        referencing the State class.
    '''
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
