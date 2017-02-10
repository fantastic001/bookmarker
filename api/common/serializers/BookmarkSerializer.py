

from rest_framework import serializers

from common.models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        read_only_fields = ["author"]
        fields = ["id", "title", "link", "author", "content"]
