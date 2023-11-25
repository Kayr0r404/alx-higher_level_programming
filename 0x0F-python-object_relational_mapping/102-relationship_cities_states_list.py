#!/usr/bin/python3
"""lists all City objects from the database"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == '__main__':
    usr, passwd, mydb = argv[1], argv[2], argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        usr, passwd, mydb))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    query = session.query(State.name, City.id, City.name).join(
        City).order_by(City.id).all()
    for i in query:
        print("{}: {} -> {}".format(i[1], i[2], i[0]))
