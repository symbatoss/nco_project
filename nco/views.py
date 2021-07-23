from django.contrib.auth import login
from rest_framework.authtoken.admin import User

from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.views import APIView

from nco.models import News, Laws, Posts, Favourites
from nco.serializer import NewsListSerializer, LawsListSerializer, PostsListSerializer, FavouritesItemSerializer, UserRegisterSerializer


class NewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsViewItem(generics.GenericAPIView):
    serializer_class = NewsListSerializer

    def get(self, request, id):
        serializer = self.get_serializer(News.objects.filter(id=id).first(), context={"request": request})
        return Response(data=serializer.data)


class LawsView(generics.ListAPIView):
    queryset = Laws.objects.all()
    serializer_class = LawsListSerializer


class LawsViewItem(generics.GenericAPIView):
    serializer_class = LawsListSerializer

    def get(self, request, id):
        serializer = self.get_serializer(Laws.objects.filter(id=id).first())
        return Response(data=serializer.data)


class PostsViewItem(generics.GenericAPIView):
    serializer_class = PostsListSerializer

    def get(self, request, category):
        serializer = self.get_serializer(Posts.objects.filter(category__name=category).first())
        return Response(data=serializer.data)


class FavouritesItem(generics.GenericAPIView):
    queryset = ""
    serializer_class = FavouritesItemSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Favourites.objects.filter(user=request.user), many=True)
        return Response(data=serializer.data)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    'message': 'ERROR',
                    'error': serializer.errors
                }
            )
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(
            username=username,
            password=password,
            is_active=False
        )
        return Response(data={'message': 'OK'})

