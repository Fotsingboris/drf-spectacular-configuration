from django.shortcuts import render

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Posts"])
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
def api_docs_home(request):
    return render(request, "blog/api_docs_home.html")