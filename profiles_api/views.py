from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View."""
    def get(self,request, format=None):
        """Returns a list of API View features"""
        an_apiview = [
        'Uses HTTP methods and function (get,post,put,patch and delete)',
        'Is similar to traditional Django View',
        'Gives you most control over application Logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview}) #Every function for api view must return a response object.

        
