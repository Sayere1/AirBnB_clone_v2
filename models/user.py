#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        first_name = Column(String(128))
        last_name = Column(String(128))
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)

        places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
