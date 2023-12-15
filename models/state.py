#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import shlex


class State(BaseModel, Base):
    """Table for the State class.

    Attributes:
        name (str): The name of the state.
        cities (relationship): Relationship to City model.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities_relation = relationship("City", cascade='all, delete, delete-orphan',
                                   backref="state")

    @property
    def cities(self):
        """Return the cities of the current state."""
        all_cities = models.storage.all(City)
        state_cities = [city for city in all_cities.values() if city.state_id == self.id]
        return state_cities
