from rest_framework import serializers

#Serializer will also take care of validation for input received
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length = 20)
