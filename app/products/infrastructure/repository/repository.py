from app.products.domain.interfaces.repository_interface import ProductRepositoryInterface
from django.contrib.auth.models import User


class ProductRepository(ProductRepositoryInterface):

    def getAll(self):
        return User.objects.all()
    
    def getById(self, id):
        pass

    def getPaginated(self):
        pass

    def create(self, userData):
        pass

    def update(self, id, userData):
        pass

    def delete(self, id):
        pass