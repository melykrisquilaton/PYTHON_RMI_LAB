
import Pyro5.api


@Pyro5.api.expose
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price
