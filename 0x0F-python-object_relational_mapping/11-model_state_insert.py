#!/usr/bin/python3
"""adds the State object “Louisiana” to the database """

from model_state import Base, State
from sqlalchemy import (create_engine)
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
    s = Session()
    n_state = State(name='Louisiana')
    s.add(n_state)
    new_inst = s.query(State).filter_by(name='Louisiana').first()
    print(new_inst.id)
    s.commit()
    s.close()
