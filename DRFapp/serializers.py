from rest_framework import serializers
from .models import Artist, Genre, Movie, MovieArtist, User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ValidationError
from .backends import CustomBackend
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):    
    password = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email','mobile','password', 'is_staff', 'is_superuser', 'is_active']
       
    def validate_password(self, password):
        return make_password(password) 

    def validate_mobile(self, mobile):
        if len(str(mobile))!=10:
            raise ValidationError("Mobile Number Must Be 10 Digit")
        return mobile

    def validate_email(self, email):
        if '@' not in str(email):
            raise ValidationError("invalid email")
        return email


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'mobile','password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         print('validated_data:',validated_data)
#         user = User.objects.create_user(validated_data['email'], validated_data['mobile'], validated_data['password'])
#         return user
        
class LoginSerializer(serializers.ModelSerializer):
    # email = serializers.CharField(max_length=50)
    # password = serializers.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
    # def validate(self,data):
    #     # print('data',data)
    #     email = data.get("email")
    #     password = data.get("password")
    #     # print('email',email)
    #     # print('password',password)
    #     try:
    #         user = authenticate(email = email, password = password)
    #         print('user(verified):',user)
    #     except:
    #         # print('email',email)
    #         pass
            
    #     # user = authenticate(**data)
    #     print(user)
    #     if user:
    #         # return redirect('DRFapp:register')
    #         return data
    #     raise serializers.ValidationError('Incorrect Credentials Passed.')
    # # data={'email':email,'password':password}
    # # validate(request,data)
    
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','language','duration','release','country','description','genre','image']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name']

class MovieArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieArtist
        fields = ['id','movie','artist','a_type']

