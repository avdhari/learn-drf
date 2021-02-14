from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    
    name = serializers.CharField(max_length=10)
