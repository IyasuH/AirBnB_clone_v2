#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
import os
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def reviews(self):
            """
            getter attribute that return the list of Review
            instances with place_id equal to the current Place.id
            """
            list_reviews = []
            for key, value in list(models.storage.all(Review)):
                if value.place_id == self.id:
                    list_reviews.append(value)
            return list_reviews
