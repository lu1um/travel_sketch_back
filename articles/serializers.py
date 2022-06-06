from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment, Region, Tag, News


class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username', 'nickname', 'picture', 'introduce', 'following',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username', 'nickname', 'picture', 'introduce', 'following',)

    class RegionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Region
            fields = '__all__'

    class TagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = '__all__'

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True)
    region = RegionSerializer(many=True)
    tag = TagSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    class RegionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Region
            fields = '__all__'

    region = RegionSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'