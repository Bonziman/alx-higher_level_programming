#!/usr/bin/python3
"""Script that lists all State objects from a db"""
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from urllib.parse import quote_plus


if __name__ == "__main__":
    usr = sys.argv[1]
    passw = quote_plus(sys.argv[2])
    dbase = sys.argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             sys.argv[1], quote_plus(sys.argv[2]), sys.argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = delete(State).where(State.name.like('%a%'))
    session.execute(stmt)
    session.commit()
