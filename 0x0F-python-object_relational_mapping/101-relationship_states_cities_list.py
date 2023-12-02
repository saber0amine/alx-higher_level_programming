#!/usr/bin/python3
""" lists all State objects, and corresponding City objects"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
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
        for inst in session.query(State).order_by(State.id):
            print(inst.id, inst.name, sep=": ")
            for city_ins in inst.cities:
                print("    ", end="")
                print(city_ins.id, city_ins.name, sep=": ")
