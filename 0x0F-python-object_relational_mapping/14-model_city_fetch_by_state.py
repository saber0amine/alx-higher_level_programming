#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_14_usa
    with state name
"""
from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    session = sessionmaker(bind=engine)()
    for c_id, c_n, s_n in session.query(
            City.id, City.name, State.name).join(State).order_by(City.id):
        print("{}: ({}) {}".format(s_n, c_id, c_n))
