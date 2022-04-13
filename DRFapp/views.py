from tokenize import Token
from .models import Artist, Genre, Movie, MovieArtist, User
from .serializers import (ArtistSerializer, GenreSerializer,
    LoginSerializer, MovieArtistSerializer, MovieSerializer, UserSerializer)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
class UserAPIView(APIView):
    """In User class implement UserAPIView using APIView
    In this class implement GET, PUT, PATCH, DELETE methods 
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['email', 'mobile']
    def get(self, request, pk=None, format=None):
        user = User.objects.filter(id=pk)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = User.objects.filter(id=pk).first()
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    def patch(self, request, pk, format=None):
        user = User.objects.filter(id=pk).first()
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        user = User.objects.filter(id=pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)


class SignUpAPI(GenericAPIView):
    """In this class make SignUpApi which is inherit from GenericAPIView
    this class make for user registration purpose
    also use knox authentication for generate token"""
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": token[1]
        })


class SignInAPI(KnoxLoginView):
    """SignUpApi inherits from KnoxLoginView
    in SignInApi check login credential or return exception error
    if credential is invalid"""
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(SignInAPI, self).post(request, format=None)


class GenreAPIView(APIView):
    """This GenreAPIView class is inherits from ApiView
    In this class implement GET, POST, PUT, PATCH, DELETE methods
    """

    def get(self, request, pk=None, format=None):
        print(request.data)
        genre = Genre.objects.filter(id=pk)
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, pk, format=None):
        genre = Genre.objects.filter(id=pk).first()
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    def patch(self, request, pk, format=None):
        genre = Genre.objects.filter(id=pk).first()
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        genre = Genre.objects.filter(id=pk)
        genre.delete()
        return Response(status=status.HTTP_200_OK)


class MovieAPIView(APIView):
    """This MovieAPIView class is inherits from ApiView
    In this class implement GET, POST, PUT, PATCH, DELETE methods
    """
    def get(self, request, pk=None, format=None):
        movie = Movie.objects.filter(id=pk)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        movie = Movie.objects.filter(id=pk).first()
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        movie = Movie.objects.filter(id=pk).first()
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, pk, format=None):
        movie = Movie.objects.filter(id=pk)
        movie.delete()
        return Response(status=status.HTTP_200_OK)


class ArtistAPIView(APIView):
    """This ArtistAPIView class is inherits from ApiView
    In this class implement GET, POST, PUT, PATCH, DELETE methods
    """
    def get(self, request, pk=None, format=None):
        artist = Artist.objects.filter(id=pk)
        serializer = ArtistAPIView(artist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        artist = Artist.objects.filter(id=pk).first()
        serializer = ArtistSerializer(artist, data=request.data)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        artist = Artist.objects.filter(id=pk).first()
        serializer = ArtistSerializer(artist, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, pk, format=None):
        artist = Artist.objects.filter(id=pk)
        artist.delete()
        return Response(status=status.HTTP_200_OK)


class MovieArtistAPIView(APIView):
    """This MovieArtistAPIView class is inherits from ApiView
    In this class implement GET, POST, PUT, PATCH, DELETE methods
    """
    def get(self, request, pk=None, format=None):
        movieartist = MovieArtist.objects.filter(id=pk)
        serializer = MovieArtistAPIView(movieartist, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = MovieArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        movieartist = MovieArtist.objects.filter(id=pk).first()
        serializer = MovieArtistSerializer(movieartist, data=request.data)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        movieartist = MovieArtist.objects.filter(id=pk).first()
        serializer = ArtistSerializer(movieartist, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, pk, format=None):
        movieartist = MovieArtist.objects.filter(id=pk)
        movieartist.delete()
        return Response(status=status.HTTP_200_OK)