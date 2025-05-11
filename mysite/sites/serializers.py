from  rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','first_name','last_name',
                  'phone_number', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.usrname,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields = '__all__'


class PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model= Property
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = '__all__'


class PhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model= Photos
        fields = '__all__'
