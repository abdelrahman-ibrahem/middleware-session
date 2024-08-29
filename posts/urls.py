from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/create/', views.create_post),
    path('posts/update/', views.update_post),
    path('posts/delete/', views.delete_post),
    path('generics/', views.PostList.as_view()),
    path('generics/<int:pk>/', views.PostDetailUpdateDelete.as_view()),
    path('logs/', views.LogList.as_view())
]