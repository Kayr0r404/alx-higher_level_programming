#!/usr/bin/python3
'''contains the class definition of a City'''

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    '''create table'''
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
