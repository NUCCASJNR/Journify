from django.urls import path
from blog.views.user_api_view import UserListView, PostUserView, GetUserWithIdView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/new/', PostUserView.as_view()),
    path('user/<uuid:user_id>/', GetUserWithIdView.as_view()),
]