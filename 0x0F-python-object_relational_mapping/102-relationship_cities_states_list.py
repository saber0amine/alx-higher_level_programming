#!/usr/bin/python3
"""list all cities with states using backref
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    session = sessionmaker(bind=engine)()
    cities = session.query(City).order_by(City.id)
    for c in cities:
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))
