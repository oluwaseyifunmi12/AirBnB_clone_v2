#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if not hasattr(self, 'id'):
            self.id = str(uuid4())
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.utcnow()
        if not hasattr(self, 'updated_at'):
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        data = {key: value for key, value in self.__dict__.items()}
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

    def delete(self):
        """ delete an object """
        models.storage.delete(self)
