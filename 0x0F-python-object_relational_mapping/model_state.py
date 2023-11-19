#!/usr/bin/python3
'''first Alchemy class'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Will document later'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128))
