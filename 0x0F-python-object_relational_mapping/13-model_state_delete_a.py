#!/usr/bin/python3
"""script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)
    session.commit()
