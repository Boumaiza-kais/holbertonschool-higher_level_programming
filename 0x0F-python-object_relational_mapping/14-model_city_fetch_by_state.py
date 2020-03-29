#!/usr/bin/python3
""" Python file similar to model_state.py named model_city.py
that contains the class definition of a City. """

import sqlalchemy
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    session = Session(engine)
    k = session.query(
        City, State).filter(City.state_id == State.id).order_by(City.id)
    for city, state in k:
        print('{}: ({}) {}'.format(state.name,
                                   city.id, city.name))
    session.close()
