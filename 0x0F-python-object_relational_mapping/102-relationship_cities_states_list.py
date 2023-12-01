#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""

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
        for instance in session.query(State).order_by(State.id):
            for city_ins in instance.cities:
                print(city_ins.id, city_ins.name, sep=": ", end="")
                print(" -> " + instance.name)
