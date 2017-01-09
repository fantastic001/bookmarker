

from rest_framework import viewsets
from common.models import Profile
from common.serializers import ProfileSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    @list_route()
    def profile(self, request):
        serializer = self.get_serializer(Profile.objects.get(user=request.user.pk))
        return Response(serializer.data)
