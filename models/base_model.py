#!/usr/bin/python3

"""
Class BaseModel:  
    v0: 

"""
class BaseModel():
    """
    BaseModel -- 
        x
    """
    def __init__():
        self.id=str(uuid.uuid4())
        self.created_at= ""
        self.updated_at= "z"

    def __str__(self):
        return "[{}] ({}) {}".format(self.id, self.id, self.__dict__)

    def __dict__(self):
        pass

    def save(self):
        self.updated_at= "x"
        return None
    def to_dict(self):
        return None
