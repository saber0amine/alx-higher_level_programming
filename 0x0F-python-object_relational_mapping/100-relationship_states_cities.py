#!/usr/bin/python3
"""creates the State
“California” with the City
“San Francisco” from
the database hbtn_0e_100_usa"""

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
        newState = State(name='California')
        newCity = City(name='San Francisco')
        newState.cities.append(newCity)
        session.add(newState)
        session.commit()
