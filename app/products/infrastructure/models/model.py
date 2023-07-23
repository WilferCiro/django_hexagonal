from django.db import models

from app.shared.infraestructure.models.base_model import BaseModel

class ProductModel(BaseModel):
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=30)