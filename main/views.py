from django.shortcuts import render, get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request

@api_view(http_method_names=["GET"])
def post_list_api_view(request: Request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    response = {"message": "Get all posts!",
                "data": serializer.data,
    }
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["POST"])
def post_create_api_view(request: Request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {"message": "Post created!",
                    "data": serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
{
    "title": "3-post",
    "content": "3-post content",
    "price": 1000,
    "count":10
}
"""


@api_view(http_method_names=["PUT"])
def post_update_api_view(request: Request, pk: int):
    post = get_object_or_404(Post, pk=pk)

    data = request.data
    serializer = PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
        response = {"message": "Post updated!",
                        "data": serializer.data}

        return Response(data=response, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(http_method_names=["DELETE"])
def post_delete_api_view(request: Request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
