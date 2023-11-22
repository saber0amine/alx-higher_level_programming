#!/usr/bin/python3
"""lists one State objects from the database hbtn_0e_6_usa
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
    result = session.query(State.id, State.name).first()
    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")
