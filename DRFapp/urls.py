from argparse import Namespace
from posixpath import basename
from unicodedata import name
from django.db import router
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 
# from DRFapp.views import MyObtainTokenPairView
from knox import views as knox_views
from .views import SignUpAPI, SignInAPI 
from DRFapp import views

urlpatterns = [  
    path('register/', SignUpAPI.as_view(), name= 'register'),
    path('login/', SignInAPI.as_view(), name='login'),
    path('logout/',knox_views.LogoutView.as_view(), name="knox-logout"),  
    path('userdetail/',views.UserAPIView.as_view()),
    path('userdetail/<int:pk>/',views.UserAPIView.as_view()),
    path('genre/',views.GenreAPIView.as_view()),
    path('genre/<int:pk>/',views.GenreAPIView.as_view()),
    path('movie/',views.MovieAPIView.as_view()),
    path('movie/<int:pk>/',views.MovieAPIView.as_view()),
    path('artist/',views.ArtistAPIView.as_view()),
    path('artist/<int:pk>/',views.ArtistAPIView.as_view()),
    path('movieartist/',views.MovieArtistAPIView.as_view()),
    path('movieartist/<int:pk>/',views.MovieArtistAPIView.as_view()),
]


# router = DefaultRouter()
# router.register('user',views.UserCreateView, basename= 'user')
# router.register('genre',views.GenreCreateView, basename= 'genre')
# router.register('movie', views.MovieCreateView, basename= 'movie')
# router.register('artist', views.ArtistCreateView, basename= 'artist')
# router.register('movieartist', views.MovieArtistCreateView, basename= 'movieartist')
# urlpatterns = [    
#     path('', include(router.urls)), 
#     path('auth/', include('rest_framework.urls', namespace= 'rest_framework')),
#     path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
#     # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
# ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    