#!/usr/bin/python3
'''prints all City objects from the database'''

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    usr, passwd, mydb = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}".format(
        usr, passwd, 3306, mydb))
    Base.metadata.create_all(engine)

    db_session = sessionmaker(bind=engine)()

    query = db_session.query(State.name, City.id, City.name).join(
        City).order_by(City.id).all()
    print(query)
    for i in query:
        print("{}: ({}) {}".format(i[0], i[1], i[2]))
