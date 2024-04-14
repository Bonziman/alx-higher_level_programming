#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base
from urllib.parse import quote_plus
from model_city import City


if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], quote_plus(sys.argv[2]), sys.argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        print(city.state.name, ":", city.id, city.name)
