

from rest_framework import viewsets
from common.models import Bookmark, Profile
from common.serializers import BookmarkSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(author=Profile.objects.get(user=self.request.user.pk))
    
