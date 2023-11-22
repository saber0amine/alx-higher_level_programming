#!/usr/bin/python3
"""searches a State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    session = sessionmaker(bind=engine)()
    result = session.query(State).order_by(State.id).filter(
                State.name == func.binary(argv[4])
            ).first()
    if result:
        print("{}".format(result.id))
    else:
        print("Not found")
