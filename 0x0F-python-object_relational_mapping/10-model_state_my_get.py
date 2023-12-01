#!/usr/bin/python3
"""prints the State object with the name"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:\
        3306/{}'.format(usrname, passwd, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    inst = s.query(State).filter(State.name == (state_name,))
    try:
        print(inst[0].id)
    except IndexError:
        print("Not found")
