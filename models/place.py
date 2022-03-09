#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import os
import models

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))



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
    amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)
    
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
        @property
        def amenities(self):
            """
            getter attribute that return the list of Amenity instance
	    based on attribute amenity_ids that contains all Amenity.id linked
	    to the place
            """
            list_amenity = []
            for key, value in list(models.storage.all(Amenity)):
                if value.id in self.amenity_ids:
                    list_amenity.append(value)
            return list_amenity
        @amenities.setter
        def amenities(self, obj):
            """
            setter attribute that handles append method for adding an
            Amenity.id to the attribute amenity_ids. should accept only
            Amenity object otherwise do nothing
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(value.id)
