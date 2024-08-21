from django.urls import path, include

urlpatterns = [
        path('blog/', include(('social_media.blog.urls', 'blog'))),
        path('user/', include(('social_media.users.urls', 'user'))),
        path('auth/', include(('social_media.authentication.urls', 'auth')))
]
