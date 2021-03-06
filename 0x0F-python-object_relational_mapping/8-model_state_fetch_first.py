#!/usr/bin/python3
""" script that prints the first State object
 from the database hbtn_0e_6_usa """


import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    session = Session(engine)
    firstst = session.query(State).order_by(State.id).first()
    if firstst:
        print("{}: {}".format(firstst.id, firstst.name))
    else:
        print("Nothing")
    session.close()
