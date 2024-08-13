from django.urls import path, include
from social_media.blog.apis.products import ProductApi

urlpatterns = [
        path('blog/', ProductApi.as_view(), name="product"),
]
