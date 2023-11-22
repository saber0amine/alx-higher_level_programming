#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
    whose name contains lowercase a
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    session = sessionmaker(bind=engine)()
    for _id, _name in session.query(
                State.id, State.name
            ).order_by(State.id).filter(
                State.name.contains('a')
            ):
        print("{}: {}".format(_id, _name))
