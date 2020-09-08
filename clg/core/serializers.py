from rest_framework import serializers
from .models import Book, User
# from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)

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