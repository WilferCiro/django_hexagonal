from functools import wraps
from rest_framework.response import Response
from rest_framework import status 

from app.shared.infraestructure.utils.custom_response import CustomResponse

def validate_request_data(serializer_class):
    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            dataIn = None
            if request.method == 'GET':
                if not request.GET:
                    return CustomResponse({'error': 'No se proporcionaron parámetros en la petición GET.'}, status=status.HTTP_400_BAD_REQUEST)
                serializer = serializer_class(data=request.GET)
                if not serializer.is_valid():
                    return CustomResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                dataIn = serializer.data
            else:
                if not request.body:
                    return CustomResponse({'error': 'No se proporcionó un cuerpo en la petición.'}, status=status.HTTP_400_BAD_REQUEST)
                serializer = serializer_class(data=request.body)
                if not serializer.is_valid():
                    return CustomResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                dataIn = serializer.data
            return view(request, dataIn, *args, **kwargs)
        return wrapper
    return decorator