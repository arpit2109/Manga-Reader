from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, MangaViewSet, ChapterViewSet, CommentViewSet, BookmarkViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'manga', MangaViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')

urlpatterns = [
    path('', include(router.urls)),
]
