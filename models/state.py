#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state')
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """getter for cities with the same
            state with the current instance
            """
            city_list = []
            # Import the 'storage' object inside the method
            from models import storage
            all_cities = models.storage.all(City)
            for key, city in all_cities.items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
