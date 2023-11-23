#!/usr/bin/python

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    usr, passwd, mydb = sys.argv[1], sys.argv[2], sys.argv[3]

    # Corrected the engine URL format
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        usr, passwd, mydb), echo=True)

    # Bind the engine to the Base
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Corrected the City instance creation
        california_city = City(name='San Francisco')
        session.add(california_city)

        # Corrected the State instance creation with relationship to the City
        california_state = State(name='California', cities=[california_city])
        session.add(california_state)

        session.commit()
        # print("Successfully created the state 'California' with the city 'San Francisco'.")

    except Exception as e:
        # print(f"Error: {e}")
        session.rollback()

    finally:
        # Close the session
        session.close()
