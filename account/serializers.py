from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        read_only_fields = ["id", "username"]
        extra_kwargs = {"password": {"write_only": True}}


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password", "password2"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("User Already exists!")
        return username

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError("Both passwords must match")
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError("Email already taken!")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
