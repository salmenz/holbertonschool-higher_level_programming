#!/usr/bin/python3
"""
Write a script that adds the State object Louisiana to the db hbtn_0e_6_usa
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
    session = Session()
    state = State(name="louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
