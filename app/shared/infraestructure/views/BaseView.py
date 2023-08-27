from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class BaseView(APIView):

    def response(self, data, state=status.HTTP_200_OK):
        if type(data) == list and len(data) == 0:
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        return Response(data, state)