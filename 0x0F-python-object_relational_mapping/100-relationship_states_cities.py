#!/usr/bin/python3
'''create relations'''

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    usr, passwd, mydb = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        usr, passwd, mydb), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    session.add(new_state)
    session.commit()

    california_city = City(name='San Francisco', state_id=new_state.id)
    session.add(california_city)
    session.commit()

    session.close()
