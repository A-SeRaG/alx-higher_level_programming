#!/usr/bin/python3
"""
This script lists all State objects
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
