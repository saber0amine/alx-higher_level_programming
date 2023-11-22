#!/usr/bin/python3
""" define state model """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State
Base = declarative_base()


class City(Base):
    """ State class """

    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey(State.id))
