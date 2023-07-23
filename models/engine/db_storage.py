#!/usr/bin/python3
""" database storage module.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage():
    """ database storage class.
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Create engine.
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database,
                                              pool_pre_ping=True))
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session.
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """ add the object to the current session.
        """
        self.__session.add(obj)

    def save(self):
        """ commit change to the current session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables and create a new session.
        """
        Base.metadata.create_all(self.__engine)
        Session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_fact)
        self.__session = Session()

    def close(self):
        """close the current session.
        """
        self.__session.close()
