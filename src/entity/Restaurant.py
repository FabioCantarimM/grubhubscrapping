import json

class Restaurant:
    def __init__(self, info, menu, options) -> None:
       self.__infos = info
       self.__menu = menu
       self.__options = options

    def toJson(self):
        return {
            "infos": self.__infos,
            "Menu": self.__menu,
            "Options": self.__options
        }

    def watch(self):
        result = self.toJson();
        print(json.dumps(result))
    
    def get(self):
        result = self.toJson();
        return json.dumps(result)
