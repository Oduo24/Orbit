#!/user/bin/python3
"""Base model module. To be inherited by all the models"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()
time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Defines the base class to be inherited by other models"""
    id = Column(String(100), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """This is the class constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()

    def __str__(self):
        """String representation of an object of this class"""
        return "[{}.{}]=>{}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves the object to the database"""
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Converts the object to a python dictionary"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
            new_dict["__class__"] = self.__class__.__name__

        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
    

    def delete(self):
        "Deletes an object"
        storage.delete(self)



