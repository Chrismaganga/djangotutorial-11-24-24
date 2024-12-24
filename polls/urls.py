from django.urls import path
from .views import (
    UserListCreateView,
    ProfileListCreateView,
    CategoryListCreateView,
    TagListCreateView,
    PostListCreateView,
    QuestionListCreateView,
    ChoiceListCreateView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('choices/', ChoiceListCreateView.as_view(), name='choice-list-create'),
]