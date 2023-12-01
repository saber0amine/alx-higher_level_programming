#!/usr/bin/python3
"""Contains State class and Base"""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mt_data = MetaData()
Base = declarative_base(metadata=mt_data)


class State(Base):
    """
    Class that defines State
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
