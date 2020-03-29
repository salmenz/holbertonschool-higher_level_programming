#!/usr/bin/python3
"""
prints the State with the name passed as argument from the db hbtn_0e_6_usa
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
    state = Session().query(State).filter(State.name == sys.argv[4]).first()
    if not state:
        print("Not found")
    else:
        print("{}".format(state.id))
    Session().close()
