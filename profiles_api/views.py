from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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


class HelloViewSet(viewsets.ViewSet):
    """
    Mainly used for model related functions,
    Automatically urls are created with the help of Routers,
    Easy for Creating for models with lesser codes.
    """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        an_viewset = [
            'Uses  functions as methods:-',
            'LIST',
            'CREATE',
            'UPDATE',
            'PARTIAL_UPDATE',
            'DESTROY',
        ]
        return Response({'Message': 'ViewSet', 'Data': an_viewset}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !!!'
            return Response({'Message': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'Message': 'HTTP method get.'})

    def update(self, request, pk=None):
        return Response({'Message': 'HTTP method put.'})

    def partial_update(self, request, pk=None):
        return Response({'Message': 'HTTP method patch.'})

    def destroy(self, request, pk=None):
        return Response({'Message': 'HTTP method delete.'})


class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
