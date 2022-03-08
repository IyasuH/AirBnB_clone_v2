#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def cities(self):
            """
            getter attribute that return the list of City
            instances with state_id equals to the current State.id
            """
            list_cities = []
            for key, value in list(models.storage.all(City)):
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities
