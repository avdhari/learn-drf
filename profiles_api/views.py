from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializers
    
    def get(self, request, format=None):
        """Returns the list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Mapped to URLs manually',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""
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
    

    def put(self, request, pk=None):
        """Handles updating object"""
        return Response({'method':'PUT'})

    
    def patch(self, request, pk=None):
        """Handles partial updates of a object"""
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})