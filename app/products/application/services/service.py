from app.products.domain.interfaces.service_interface import ProductServiceInterface

class ProductService(ProductServiceInterface):
    
    def getAll(self):
        return self.productRepository.getAll()
    
    def getById(self, id):
        pass

    def getPaginated(self):
        pass

    def create(self, data):
        return self.productRepository.create(data)

    def update(self, id, data):
        pass

    def delete(self, id):
        pass