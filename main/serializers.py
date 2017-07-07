from rest_framework import serializers
from .models import PostsModel,CommentsModel


class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostsModel
        fields = '__all__'


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = '__all__'