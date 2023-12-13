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
    CountAllPostViews,
    ListAUserBlogPosts,
    GetBlogPostView,
    GetOneBlogPostOfAUserView,
    DeleteBlogPostsView
)
from blog.views.signup import home, signup
from blog.views.login import login, dashboard, logout
urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/new/', PostUserView.as_view()),
    path('user/<uuid:user_id>/', GetUserWithIdView.as_view()),
    path('del_user/<uuid:user_id>/', DeleteUserWithIdView.as_view()),
    path('update_user/<uuid:user_id>/', UpdateUserWithIdView.as_view()),
    path('posts/', BlogListView.as_view()),
    path('post/new/', BlogAddView.as_view()),
    path('posts_count/', CountAllPostViews.as_view()),
    path('users_count/', ListTotalNumberOfUsers.as_view()),
    path('user_blogs/<str:user_id>/', ListAUserBlogPosts.as_view()),
    path('post/<uuid:post_id>/', GetBlogPostView.as_view()),
    path('user/<str:user_id>/singlepost/<str:post_id>/', GetOneBlogPostOfAUserView.as_view()),
    path('del_post/<uuid:user_id>/', DeleteBlogPostsView.as_view()),
    path('', home, name='home'),
    path('auth/signup', signup, name='signup'),
    path('auth/login', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout', logout, name='logout')
]
