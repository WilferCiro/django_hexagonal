from django.urls import include, path
from app.products.infrastructure.views.views import ProductViewSet
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('users', csrf_exempt(ProductViewSet.as_view())),
    path('api', include('rest_framework.urls', namespace='rest_framework')),
]