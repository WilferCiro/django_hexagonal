from rest_framework.response import Response
from rest_framework import status as status_codes

def CustomResponse(data, status=status_codes.HTTP_200_OK):
    if type(data) == list and len(data) == 0:
        return Response(data, status=status_codes.HTTP_204_NO_CONTENT)
    return Response(data, status)