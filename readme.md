
---

### **Introduction**




### **1. Create a Django Project**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install django djangorestframework drf-spectacular
django-admin startproject config .
```

Run server to confirm:

```bash
python manage.py runserver
```

👉 Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to check.

---

### **2. Create a Django App**

```bash
python manage.py startapp blog
```

Add to **settings.py**:

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "drf_spectacular",
    "blog",
]
```

---

### **3. Create a Simple Model**

In `blog/models.py`:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **4. Create Serializer**

In `blog/serializers.py`:

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
```

---

### **5. Create API View**

In `blog/views.py`:

```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Posts"])
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

---

### **6. Add API Routes**

In `config/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from blog.views import PostListCreateView
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
]
```

---

### **7. Configure DRF & Spectacular**

In `config/settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Blog API",
    "DESCRIPTION": "Simple API demo using Django Spectacular",
    "VERSION": "1.0.0",
}
```

---

### **8. Test the API**

1. Start server:

   ```bash
   python manage.py runserver
   ```
2. Visit:

   * `http://127.0.0.1:8000/api/posts/` → API endpoint (CRUD posts)
   * `http://127.0.0.1:8000/api/schema/` → OpenAPI schema JSON
   * `http://127.0.0.1:8000/api/docs/` → Swagger UI
   * `http://127.0.0.1:8000/api/redoc/` → Redoc UI

---


a **simple HTML page** that lists your 3 API documentation endpoints (**Schema JSON**, **Swagger UI**, and **Redoc**) in a professional way using **Bootstrap**, 
---

## **1. Create a Function-Based View**

In `blog/views.py`:

```python
from django.shortcuts import render

def api_docs_home(request):
    return render(request, "blog/api_docs_home.html")
```

---

## **2. Add the URL**

In `config/urls.py`:

```python
from django.urls import path
from blog.views import api_docs_home

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
```


---

## **3. Create the HTML Template**

Create a file `blog/templates/blog/api_docs_home.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Documentation</title>
    <!-- Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

    <div class="container py-5">
        <div class="text-center mb-4">
            <h1 class="fw-bold">API Documentation</h1>
            <p class="text-muted">Explore different API formats for this project</p>
        </div>

        <div class="row justify-content-center g-4">
            <!-- OpenAPI Schema -->
            <div class="col-md-4">
                <div class="card shadow-sm border-0 h-100">
                    <div class="card-body text-center">
                        <h5 class="card-title">OpenAPI Schema</h5>
                        <p class="card-text">Raw OpenAPI JSON schema for integrations.</p>
                        <a href="{% url 'schema' %}" class="btn btn-primary w-100">View Schema</a>
                    </div>
                </div>
            </div>

            <!-- Swagger UI -->
            <div class="col-md-4">
                <div class="card shadow-sm border-0 h-100">
                    <div class="card-body text-center">
                        <h5 class="card-title">Swagger UI</h5>
                        <p class="card-text">Interactive documentation with Swagger.</p>
                        <a href="{% url 'swagger-ui' %}" class="btn btn-success w-100">Open Swagger</a>
                    </div>
                </div>
            </div>

            <!-- Redoc -->
            <div class="col-md-4">
                <div class="card shadow-sm border-0 h-100">
                    <div class="card-body text-center">
                        <h5 class="card-title">Redoc UI</h5>
                        <p class="card-text">Modern and user-friendly documentation with Redoc.</p>
                        <a href="{% url 'redoc' %}" class="btn btn-danger w-100">Open Redoc</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## **4. Final Result**

* Visit: **[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)**
* You’ll see a **Bootstrap grid layout** with 3 cards:

  * **OpenAPI Schema** → JSON schema
  * **Swagger UI** → interactive docs
  * **Redoc** → modern docs

---

