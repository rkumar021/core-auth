from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,  IsAuthenticated
import requests
from .models import Book
from .serializers import BookSerializer, SignUpSerializer, UpdateSerializer, DeleteSerializer, ViewSerializer
from rest_framework import generics
from .permissions import IsAuthenticatedOrCreate
# from core.serializers import BookSerializer
from .models import User

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class See(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ViewSerializer
    permission_classes = (AllowAny,)


class Update(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (IsAuthenticated,)

class Delete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DeleteSerializer
    permission_classes = (AllowAny,)