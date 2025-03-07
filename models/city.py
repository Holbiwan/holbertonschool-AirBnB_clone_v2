#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
import models
from models.place import Place
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")

def _init_init(self, *args, **kwargs):
    """initialize inerited"""
    super()._init_(*args, **kwargs)
