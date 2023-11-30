from django.urls import path
from blog.views.user_api_view import UserListView

urlpatterns = [
    path('users/', UserListView.as_view()),
]