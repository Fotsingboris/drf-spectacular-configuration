from django.contrib import admin
from django.urls import path
from blog.views import PostListCreateView, api_docs_home
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Blog API
    path("api/posts/", PostListCreateView.as_view(), name="post-list-create"),

    # API Schema & Docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    
    # Custom API Docs Homepage
    path("api/", api_docs_home, name="api-home"),
]