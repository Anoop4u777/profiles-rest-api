from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer


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

    def post(self, request):
        """Create a post without a model"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            """Below the serializer.validated_data passes orderedDict(list[(tuples)])"""
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !!!'
            return Response({'Message': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Updates the entire object.
            Example :-
            If there is 2 fields in a model a,b
            then if u put by only giving b the PUT
            will remove the value of a ie, what put does it overwrites an
            object with the key values that you pass during the using of PUT.
        """
        return Response({'Message':'PUT'})

    def patch(self, request, pk=None):
        """Updates an object partially"""
        return Response({'Message':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an entire object"""
        return Response({'Message':'DELETE'})
