from tokenize import Token
from .models import Artist, Genre, Movie, MovieArtist, User
from .serializers import ArtistSerializer, GenreSerializer, LoginSerializer, MovieArtistSerializer, MovieSerializer, UserSerializer,RegisterSerializer 
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



class UserAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request, pk= None, format = None):
        id = pk
        if id is not None:
            try:
                user = User.objects.get(id=id)
            except User.DoesNotExist:
                raise Http404()
            serializer = UserSerializer(user, many = False)
            return Response(serializer.data)
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)

    # def post(self, request, format = None):
    #     serializer = UserSerializer(data = request.data)
    #     # print(request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(status= status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id = pk 
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        id = pk
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        id= pk
        # print('pk',request.user)
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404()
        user.delete()
        return Response({'msg':'data deleted'})

class SignUpAPI(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
class SignInAPI(KnoxLoginView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        print('------------------------------------',user)
        return super(SignInAPI, self).post(request, format=None)

class GenreAPIView(APIView):
    def get(self, request, pk= None, format = None):
        id = pk
        # print(id)
        if id is not None:
            genre = Genre.objects.get(id=id)
            serializer = GenreSerializer(genre, many = False)
            return Response(serializer.data)
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = GenreSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id = pk
        genre = Genre.objects.get(id = id)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        id = pk
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        id = pk 
        genre = Genre.objects.get(id=id)
        genre.delete()
        return Response({'msg':'data deleted'})

class MovieAPIView(APIView):
    def get(self, request, pk= None, format = None):
        id = pk
        if id is not None:
            movie = Movie.objects.get(id=id)
            serializer = MovieSerializer(movie, many = False)
            return Response(serializer.data)
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = MovieSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id = pk
        movie = Movie.objects.get(id = pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        id = pk
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format = None):
        id = pk 
        movie = Movie.objects.get(id=id)
        movie.delete()
        return Response({'msg':'data deleted'})
 
class ArtistAPIView(APIView):
    def get(self, request, pk= None, format = None):
        id = pk
        if id is not None:
            artist = Artist.objects.get(id=id)
            serializer = ArtistAPIView(artist, many = False)
            return Response(serializer.data)
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ArtistSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id = pk
        artist = Artist.objects.get(id = pk)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        id = pk
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format = None):
        id = pk 
        artist = Artist.objects.get(id=id)
        artist.delete()
        return Response({'msg':'data deleted'})
 
class MovieArtistAPIView(APIView):
    def get(self, request, pk= None, format = None):
        id = pk
        if id is not None:
            movieartist = MovieArtist.objects.get(id=id)
            serializer = MovieArtistAPIView(movieartist, many = False)
            return Response(serializer.data)
        movieartist = MovieArtist.objects.all()
        serializer = MovieArtistSerializer(movieartist, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = MovieArtistSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id = pk
        movieartist = MovieArtist.objects.get(id = pk)
        serializer = MovieArtistSerializer(movieartist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        id = pk
        movieartist = MovieArtist.objects.all()
        serializer = ArtistSerializer(movieartist, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format = None):
        id = pk 
        movieartist = MovieArtist.objects.get(id=id)
        movieartist.delete()
        return Response({'msg':'data deleted'})
 
# class UserCreateView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAdminUser]

# class GenreCreateView(viewsets.ModelViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer

# class MovieCreateView(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class ArtistCreateView(viewsets.ModelViewSet):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

# class MovieArtistCreateView(viewsets.ModelViewSet):
#     queryset = MovieArtist.objects.all()
#     serializer_class = MovieArtistSerializer

# class MyObtainTokenPairView(TokenObtainPairView):
#     queryset = User.objects.filter()
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer