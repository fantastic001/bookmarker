
from rest_framework import viewsets
from common.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = serializer_class.Meta.model.objects.all()
    
