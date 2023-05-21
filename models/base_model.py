#!/usr/bin/python3
# AirBnB_clone
# Author: Ikundwila Mwambona <ikumwana@gmail.com>

import uuid
from datetime import datetime
"""
This module contains the BaseModel class, which defines common attributes for other classes.
"""


class BaseModel:
    """
    The BaseModel class serves as a base class for other modules in the project.
    It contains common attributes and methods that are inherited by other classes.
    """

    def __init__(self):
        """
        Initializes the BaseModel instance.

        Attributes:
        - id (str): Unique identifier for the instance.
        - created_at (datetime): Date and time of instance creation.
        - updated_at (datetime): Date and time of instance update.
        """
        self.id = str(uuid.uuid4())  # Assign a unique ID using uuid.uuid4()
        self.created_at = datetime.now()  # Set the creation date and time
        self.updated_at = datetime.now()  # Set the update date and time

    def __str__(self):
        """
        Return a string representation of the object.

        Format: {<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id,self.__dict__)

    def save(self):
        """
        Update the update_at attribute with the current datetime.
        :return:
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the object.

        The dictionary contains all keys/values of __dict__ of the instance,
        with additional keys '__class__', 'created_at', and 'updated_at'.
        The created_at and updated_at attribute are converted to the specified format, (%Y-%m-%dT%H:%M:%S.%f).

        Returns:
        - dict: Dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f").isoformat()
        obj_dict['updated_at'] = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f").isoformat()
        return obj_dict
