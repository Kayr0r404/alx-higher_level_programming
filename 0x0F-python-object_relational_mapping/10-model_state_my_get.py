#!/usr/bin/python3
'''lists all State objects from the database '''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    usr, passwd, mydb = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        usr, passwd, mydb))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i, n = State.id, State.name
    query = session.query(State).filter(n == sys.argv[4]).order_by(i).all()

    if query:
        for state in query:
            print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
