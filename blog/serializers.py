from .models import Blog
# from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our BlogSerializer
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Blog
        # the fields that should be included in the serialized output
        fields = ["id", "title", "body"]