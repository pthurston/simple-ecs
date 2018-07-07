import uuid
import json

class Entity(object):

    def __init__(self, id = None):
        self.id = id or uuid.uuid1().hex

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4)

    @classmethod
    def from_json(cls, json_str):
        return json.loads(json_str, object_hook=lambda x: cls(**x))
        

