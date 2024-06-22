from django.urls import path
from .views import (post_list_api_view,
                    post_create_api_view,
                    post_update_api_view,
                    post_delete_api_view)
urlpatterns = [
    path('posts/', post_list_api_view, name='posts'),
    path('post/create/', post_create_api_view, name='post-create'),
    path('post/<int:pk>/', post_update_api_view, name='post-update'),
    path('post/delete/<int:pk>/', post_delete_api_view, name='post-delete'),
]