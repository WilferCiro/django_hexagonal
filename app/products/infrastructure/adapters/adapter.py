from app.products.domain.models import Product
from app.products.infrastructure.models import ProductModel

class TaskAdapter:
    def to_domain(self, task_model: ProductModel) -> Product:
        return Product(
            id=task_model.id,
            title=task_model.title,
            price=task_model.price,
        )

    def to_model(self, task: Product) -> ProductModel:
        return ProductModel(
            id=task.id,
            title=task.title,
            price=task.price,
        )

    def to_create(self, task: Product) -> ProductModel:
        return ProductModel(
            id=task.id,
            title=task.title,
            price=task.price,
        )

    def to_update(self, task: Product) -> ProductModel:
        return ProductModel(
            id=task.id,
            title=task.title,
            price=task.price,
        )