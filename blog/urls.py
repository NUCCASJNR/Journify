from django.urls import path
from blog.views.user_api_view import (
    UserListView,
    GetUserWithIdView,
    PostUserView,
    DeleteUserWithIdView,
    UpdateUserWithIdView,
    ListTotalNumberOfUsers
)
from blog.views.blog_api_view import (
    BlogListView,
    BlogAddView,
    CountAllPostViews
)

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/new/', PostUserView.as_view()),
    path('user/<uuid:user_id>/', GetUserWithIdView.as_view()),
    path('del_user/<uuid:user_id>/', DeleteUserWithIdView.as_view()),
    path('update_user/<uuid:user_id>/', UpdateUserWithIdView.as_view()),
    path('posts/', BlogListView.as_view()),
    path('post/new/', BlogAddView.as_view()),
    path('posts_count/', CountAllPostViews.as_view()),
    path('users_count/', ListTotalNumberOfUsers.as_view())
]
