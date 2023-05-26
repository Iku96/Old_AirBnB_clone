#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:
    """
    Base class for other classes in the project.

    Public instance attributes:
        id: string - assigned with a unique UUID when an instance is created.
            The UUID is generated using the uuid.uuid4() function and then converted to a string.
        created_at: datetime - assigned with the current datetime when an instance is created.
        updated_at: datetime - assigned with the current datetime when an instance is created
            and updated every time the object is changed.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Arbitrary keyword arguments.
                Each key of the dictionary represents an attribute name, and the corresponding value
                is the value for that attribute.

        If kwargs is not empty:
            Each key-value pair in kwargs is set as an attribute of the instance.
            The 'created_at' and 'updated_at' attributes are converted from strings to datetime objects.

        Otherwise:
            A new instance is created with a unique 'id' attribute generated using uuid.uuid4() and converted to a string.
            The 'created_at' attribute is set to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the object.

        Returns:
            dict: A dictionary containing all keys/values of the instance's attributes.
                The dictionary also includes the '__class__' key with the class name of the object,
                and the 'created_at' and 'updated_at' keys with their corresponding values in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
