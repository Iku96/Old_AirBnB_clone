#!/usr/bin/python3
class FileStorage:
    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # dictionary to store all objects

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

