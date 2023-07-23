from app.products.domain.interfaces.service_interface import ProductServiceInterface

class ProductService(ProductServiceInterface):
    
    def getAll(self):
        return self.productRepository.getAll()
    
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