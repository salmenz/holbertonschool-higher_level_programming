#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    state = Session().query(State).first()
    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    Session().close()
