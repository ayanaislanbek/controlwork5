from django.urls import path
from .import views 

urlpatterns = [
    path('registration/', views.SignupView.as_view()),
    path('login', views.LoginView.as_view()),
    path('posts/', views.PostListCreateView.as_view()),
    path('post/<int:id>/', views.PostDetailView.as_view()),
    path('api/v1/posts/<int:id>/', views.CommentListCreateView.as_view())
]