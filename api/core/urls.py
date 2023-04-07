from rest_framework.routers import DefaultRouter
from core.views import MovieViewSet, GenreViewSet


router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('genres', GenreViewSet, basename='genres')

app_name = 'core'
urlpatterns = [  
]
urlpatterns += router.urls
