from rest_framework import serializers
from .models import Book, User
# from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class SignUpSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')