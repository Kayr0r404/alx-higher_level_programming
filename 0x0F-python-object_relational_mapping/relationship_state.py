#!/usr/bin/python3
'''first Alchemy class'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    '''Will document latergit add '''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128))
    cities = relationship('City', cascade="all, delete-orphan"
                          backref=backref("state", cascade="all"),
                          single_parent=True)
