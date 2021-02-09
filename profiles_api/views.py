from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns the list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Mapped to URLs manually',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})