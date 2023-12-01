#!/usr/bin/python3
"""
Contains State class and Base,
an instance of declarative_base()
"""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

mt_data = MetaData()
Base = declarative_base(metadata=mt_data)


class State(Base):
    """
    Class that defines state
    table: the name of the table.
    id: the id
    name: the name:with expression as target:
        pass
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
