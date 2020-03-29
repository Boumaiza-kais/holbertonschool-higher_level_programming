#!/usr/bin/python3
"""script that changes the name of a State object from
the database hbtn_0e_6_usa
"""

import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
