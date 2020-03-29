#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the db hbtn_0e_6_usa
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
    states = Session().query(State).filter(State.name.ilike('%a%')) \
        .order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    Session().close()
