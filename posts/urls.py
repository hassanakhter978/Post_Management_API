from django.urls import path
from posts.views import PostAPIView
from posts.views import PostAPIDetailView

urlpatterns = [
    path('api/posts', PostAPIView.as_view()),
    path('api/posts/<int:pk>/', PostAPIDetailView.as_view())
]