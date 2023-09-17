from rest_framework import serializers
from posts.models import PostAPIModel



class PostAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = PostAPIModel
        fields = "__all__"