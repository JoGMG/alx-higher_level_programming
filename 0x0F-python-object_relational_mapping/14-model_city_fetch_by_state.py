#!/usr/bin/python3
"""
This script prints all `City` objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    query = session.query(City, State).join(State)
    for c, s in query.all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
