#!/usr/bin/python3
'''
...
'''


from sqlalchemy import create_engine
from sys import argv
from model_state import State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*sys.argv[1:]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).first()

    if query is None:
        print('Nothing')
        sys.exit()

    print("{}: {}".format(query.id, query.name))

    session.close()
