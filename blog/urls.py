from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TagView, BlogView, CommentView, ImageView, TopBlogView, SpecialblogView)


router = DefaultRouter()
router.register('tag-url', TagView, basename='tag-url')
router.register('blog-url', BlogView, basename='blog-url')
router.register('comment-url', CommentView, basename='comment-url')
router.register('image-url', ImageView, basename='image-url')
router.register('top-blog-url', TopBlogView, basename='top-blog-url_list')
router.register('special-blog-url', SpecialblogView, basename='special-blog-url_list')

urlpatterns = [
	path('', include(router.urls)),
]
