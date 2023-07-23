from abc import ABC, abstractmethod

class ProductRepositoryInterface(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def getAll(self):
        pass
    
    @abstractmethod
    def getById(self, id):
        pass

    @abstractmethod
    def getPaginated(self):
        pass

    @abstractmethod
    def create(self, userData):
        pass

    @abstractmethod
    def update(self, id, userData):
        pass

    @abstractmethod
    def delete(self, id):
        pass