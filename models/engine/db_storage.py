#!/usr/bin/python3
"""
Another engine to manage the database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage():
    """
    To mange database
    """
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(os.getenv('HBNB_MYSQL_USER'),
                                                                           os.getenv('HBNB_MYSQL_PWD'),
                                                                           os.getenv('HBNB_MYSQL_HOST'),
                                                                           os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            """drop alltables"""
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query"""
        if cls is None:
            # Add up Amenity, Place, Review
            query_obj = self.__session.query(State).all()
            query_obj.extend(self.__session.query(City).all())
            query_obj.extend(self.__session.query(User).all())
            query_obj.extend(self.__session.query(Place).all())

        else:
            query_obj = self.__session.query(cls)
        for obj in query_obj:
            return {"{}.{}".format(type(obj).__name__, obj.id): obj}

    def new(self,obj):
        """ add objects to the cursent databse session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if Not None"""
        self.__session.delete(obj)

    def reload(self):
        """create all tables in the database, create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
