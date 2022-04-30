import re
from yaml import load, FullLoader
from collection.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.MULTILINE.re.compile(__delimiter)

    @classmethod
    def load(cls,string):
        __regex.split(string) = -, fm, content
        load(fm)
        Loader (FullLoader)
        return cls(metadata,content)

    def __init__(self, metadata, content):
        self.metadata = data
        self.data = {"content":content}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if self.data in ["type"]:
            return self.data["type"]
        elif self.data not in ["type"]:
            return None
    @property
    def setter(self):
        return self.data["type"]

    def __iter__(self):
        for i in self.data:
            return i

    def __len__(self):
        return len(self.data)

    def __repr__():
        data = {}
        return str(data)

    for value in self.data.items():
        if value != "content":
            value = data[key]
