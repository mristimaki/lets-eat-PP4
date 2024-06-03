from . import views
from django.urls import path
from .views import EditComment, RecipeDetail


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLikes.as_view(), name='post_likes'),
    path('edit_comment/<int:comment_id>', EditComment.as_view(), name='edit_comment'),
]
