from os import name
from django.urls import path, include
from requests.api import get
from .import views
from .views import BookViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('api/books',include(router.urls)),
    path('signup/', views.register, name="sign_up"),
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
    path('view/', views.See.as_view()),
    path('create/', views.create, name="createbook"),
    path('<pk>/update/', views.Update.as_view(), name="update"),
    path('<pk>/delete/', views.Delete.as_view(), name= "delete")

]

