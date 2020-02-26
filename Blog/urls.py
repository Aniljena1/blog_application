from django.urls import path
from Blog import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),

    path('about/', views.about,name='blog-about'),

    path('blog-python/',views.blog_python_view,name='blog-python'),

    path('latest_posts/',views.Latest_list_view,name='latest_posts'),

    path('top_questions/',views.top_questions,name='top_questions'),

]