from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            'Uses HTTP functions as methods:-',
            'GET',
            'POST',
            'PUT',
            'PATCH',
            'DELETE',
        ]

        return Response({'Message': 'Hello!!!', 'an_apiview': an_apiview})
