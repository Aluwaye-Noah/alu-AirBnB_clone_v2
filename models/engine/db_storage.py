#!/usr/bin/python3

"""file storage for database"""

import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None
