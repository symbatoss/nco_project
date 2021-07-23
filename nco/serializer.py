from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

from nco.models import News, Photos, Laws, Posts, Favourites


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = "photo".split()


class NewsListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    bool = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "id title text date link photo bool".split()

    def get_photo(self, obj):
        photo = Photos.objects.filter(news=obj)
        return PhotoSerializer(photo, many=True).data

    def get_bool(self, obj):
        try:
            fav = Favourites.objects.get(news=obj, user=self.context["request"].user)
        except Exception:
            return False
        return fav.bools


class LawsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laws
        fields = "id title text date category".split()


class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "id title text category date".split()


class FavouritesItemSerializer(serializers.ModelSerializer):
    news = NewsListSerializer()

    class Meta:
        model = Favourites
        fields = "bools news".split()


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError("Такой пользователь уже есть!")
        return username

