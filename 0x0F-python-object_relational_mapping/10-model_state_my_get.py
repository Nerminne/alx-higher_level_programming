#!/usr/bin/python3
"""lists first State objects from the database hbtn_0e_6_usa"""


from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(
            State.name == argv[4]).order_by(State.id).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()
