#!/usr/bin/python3
"""deletes all State objects with a
name containing the letter a"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:\
        3306/{}'.format(usrname, passwd, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.execute(delete(State).where(State.name.like('%a%')))
        session.commit()
