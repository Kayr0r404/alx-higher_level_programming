#!/usr/bin/python3
'''create relations'''

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    usr, passwd, mydb = sys.argv[1], sys.argv[2], sys.argv[3]

    # Corrected the engine URL format
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        usr, passwd, mydb), echo=False)

    # Bind the engine to the Base
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()

    california_state = State(name='California')
    session.add(california_state)
    session.commit()

    california_city = City(name='San Francisco', state_id=california_state.id)
    session.add(california_city)
    session.commit()

    session.close()
