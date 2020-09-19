from rest_framework import serializers
from .models import Book, User
# from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class CreateBookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book
    class Meta:
        model = Book
        fields = ('id', 'created', 'title','description', 'price')

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


class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')