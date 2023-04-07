from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin
)
from rest_framework.response import Response
from core.models import Movie, Genre
from core.serializers import MovieSerializer, GenreSerializer
from core.filters import MovieFilter, GenreFilter
from rest_framework.decorators import action
from django.db.models import Count
from rest_framework.permissions import AllowAny


class MovieViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    
    lookup_field = 'slug'
    queryset = Movie.objects.prefetch_related('genres').all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny,]
    filterset_class = MovieFilter
    search_fields = [
        'slug', 'title_fa', 
        'title_en', 'summary', 
        'genres__title', 'genres__slug'
    ]
    ordering_fields = [
        'slug', 'title_fa', 'title_en',
        'published_at', 'release_year', 
        'rate_percentage', 'imdb_rank_percent',
        'duration', 'visits'
    ]
    
    @action(
        detail=False,
        methods=['delete',], 
        url_name='delete_all', 
        url_path='delete_all'
    )
    def delete_all(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.delete()
        return Response(status=204)
    
    
class GenreViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    
    lookup_field = 'slug'
    
    # Annotate movie_count to the objects (used in the filters)
    queryset = Genre.objects.prefetch_related('movies').\
        annotate(movie_count=Count('movies')).all()
        
    serializer_class = GenreSerializer
    permission_classes = [AllowAny,]
    filterset_class = GenreFilter
    search_fields = ['slug', 'title', 'body']
    ordering_fields = ['slug', 'title', 'movie_count']
