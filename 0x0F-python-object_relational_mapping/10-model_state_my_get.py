#!/usr/bin/python3
"""..."""


import sys
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like(str(argv[4]))).first()

    if query is None:
        print('Not found')
        sys.exit()
    print("{}".format(query.id))

    session.close()
