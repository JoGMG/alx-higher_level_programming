#!/usr/bin/python3
"""
This script changes the name of a `State` object
in the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Making connection and accessing the database with sqlalchemy.
    """
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)

    Session = sessionmaker(bind=engine)
    session = Session()

    arizona = session.query(State).filter(State.id == '2').first()
    arizona.name = 'New Mexico'
    session.commit()
    session.close()
