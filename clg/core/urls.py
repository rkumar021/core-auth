from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="sign_up"),
    path('update/', views.Update.as_view(), name="update"),
    path('delete/', views.Delete.as_view(), name="delete"),
    path('book/', views.BookViewSet),
]

