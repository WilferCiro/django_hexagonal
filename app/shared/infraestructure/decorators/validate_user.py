from functools import wraps
from rest_framework import status 

from app.shared.infraestructure.utils.custom_response import CustomResponse

def validate_user(profiles=["admin"]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            
            # return CustomResponse({"error": "Permisos denegados (" + ','.join(profiles) + ")"}, status=status.HTTP_403_FORBIDDEN)
                
            return view_func(request, *args, **kwargs)

        return wrapped_view
    return decorator