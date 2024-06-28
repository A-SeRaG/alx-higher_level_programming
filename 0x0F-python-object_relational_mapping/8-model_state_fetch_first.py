#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    usrname = sys.argv[1]
    passw = sys.argv[2]
    dbname = sys.argv[3]
    db = (f'mysql+mysqldb://{usrname}:{passw}@localhost:3306/{dbname}')
    # Create a connection to the MySQL server
    engine = create_engine(db, pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    # Display the result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
    
    # Close the session
    session.close()
