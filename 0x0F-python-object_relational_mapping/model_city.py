#!/usr/bin/python3
"""Defines a City class"""

from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class City(Base):
    """Represents a City"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)

    state = relationship("State")

