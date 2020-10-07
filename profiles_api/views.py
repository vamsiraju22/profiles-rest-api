from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status     #list of http status codes used when returning responses
from profiles_api import serializer
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test API View."""
    serializer_class = serializer.HelloSerializer

    def get(self,request, format=None):
        """Returns a list of API View features"""
        an_apiview = [
        'Uses HTTP methods and function (get,post,put,patch and delete)',
        'Is similar to traditional Django View',
        'Gives you most control over application Logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview}) #Every function for api view must return a response object.

    def post(self, request):
        """Create a hello message with our name"""
        serializer =   self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
             )

    #pk =Primary Key, it takes the id of the object
    def put(self, request, pk = None): #update an existing value with the input
        """Handle updating object."""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of the object."""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object in database."""
        return Response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializer.HelloSerializer
    def list(self, request):
        """Return a hello message."""
        ...

        a_viewset = [
        'Uses Actions (list, create , retrieve, update , partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code.',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
             )

    def retrieve(self, request, pk=None):
        """Handle getting object by its ID."""
        return Response({'http_method':'GET'})


    def update(self, request, pk=None):
        """Handle updating an object ."""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object ."""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing object."""
        return Response({'http_method':'DELETE'})
