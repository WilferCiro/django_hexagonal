from app.products.domain.interfaces.repository_interface import ProductRepositoryInterface
from app.products.infrastructure.models.models import ProductModel


class ProductRepository(ProductRepositoryInterface):

    def getAll(self):
        return ProductModel.objects.all()

    def getById(self, id):
        pass

    def getPaginated(self):
        pass

    def create(self, userData):
        return ProductModel.objects.create(title=userData["title"], price=userData["price"])

    def update(self, id, userData):
        pass

    def delete(self, id):
        pass
