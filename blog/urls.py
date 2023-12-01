from django.urls import path
from blog.views.user_api_view import UserListView, PostUserView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/new/', PostUserView.as_view()),
]