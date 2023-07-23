from app.products.infrastructure.repository.repository import ProductRepository
from app.products.application.services.service import ProductService
from app.products.infrastructure.serializers_dto.serializers import ProductDtoSerializer
from app.products.application.serializers.serializers import ProductSerializer
from app.shared.infraestructure.decorators.validate_serializer import validate_request_data
from app.shared.infraestructure.decorators.validate_user import validate_user
# ValidateSerializer
from app.shared.infraestructure.views.BaseView import BaseView

class UserViewSet(BaseView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    service = None
    def __init__(self, service):
        super().__init__()
        self.service = service

    @validate_user()
    @validate_request_data(serializer_class=ProductDtoSerializer)
    def get(self, request):
        queryset = self.service.getAll()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return self.response(serializer.data)

def user_view(request):
    # Instancia los objetos de servicio y repositorio
    repository = ProductRepository()
    service = ProductService(repository)

    view = UserViewSet.as_view(service=service)
    return view(request)