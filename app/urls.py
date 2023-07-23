from django.urls import include, path
from app.products.infrastructure.views.views import product_view

urlpatterns = [
    path('users/', product_view),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]