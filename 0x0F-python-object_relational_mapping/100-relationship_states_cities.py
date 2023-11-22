#!/usr/bin/python3
"""adds rows using relationship
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    c = City(name="San Francisco")
    s = State(name="California", cities=[c])
    session.add(s)
    session.add(c)
    session.commit()
