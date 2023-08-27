from app.products.infrastructure.repository.repository import ProductRepository
from app.products.application.services.service import ProductService
from app.products.infrastructure.serializers_dto.serializers import ProductCreateDtoSerializer
from app.products.application.serializers.serializers import ProductSerializer
from app.shared.infraestructure.decorators.validate_serializer import validate_request_data
from app.shared.infraestructure.decorators.validate_user import validate_user
# ValidateSerializer
from app.shared.infraestructure.views.BaseView import BaseView
from django.utils.decorators import method_decorator
from rest_framework.decorators import action

class ProductViewSet(BaseView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    repository = ProductRepository()
    service = ProductService(repository)

    @method_decorator(validate_user())
    @method_decorator(validate_request_data(serializer_class=ProductCreateDtoSerializer))
    def get(self, request, *args):
        queryset = self.service.getAll()
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return self.response(serializer.data)
    
    @action(methods=['get'], detail=True)
    # @method_decorator(validate_user())
    def get_one(self, request, pk=None, *args, **kwargs):
        print(pk, args)
        queryset = self.service.getAll()
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return self.response(serializer.data)

    # @method_decorator(validate_user())
    @method_decorator(validate_request_data(serializer_class=ProductCreateDtoSerializer))
    def post(self, request, dataIn, *args):
        queryset = self.service.create(dataIn)
        serializer = ProductSerializer(
            queryset, context={'request': request})
        return self.response(serializer.data)

    # @method_decorator(validate_user())
    # @method_decorator(validate_request_data(serializer_class=ProductCreateDtoSerializer))
    def put(self, request, id, *args, **kwargs):
        #queryset = self.service.create()
        #serializer = ProductSerializer(
        #    queryset, context={'request': request})
        return self.response({}) #serializer.data)
