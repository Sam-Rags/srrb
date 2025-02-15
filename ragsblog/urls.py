from django.urls import path, include
from django.conf import settings

from . import views
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name="post_draft_list"),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/unpublish/', views.post_unpublish, name='post_unpublish'),
    path('media/<int:pk>/', views.img_full, name='img_full'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)