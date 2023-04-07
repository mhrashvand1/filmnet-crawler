from django_filters import rest_framework as filters
from core.models import Movie, Genre


class MovieFilter(filters.FilterSet):
    
    published_at__lt = filters.DateTimeFilter(field_name='published_at', lookup_expr='lt')
    published_at__gt = filters.DateTimeFilter(field_name='published_at', lookup_expr='gt')

    release_year__lt = filters.NumberFilter(field_name='release_year', lookup_expr='lt')
    release_year__gt = filters.NumberFilter(field_name='release_year', lookup_expr='gt')

    rate_percentage__lt = filters.NumberFilter(field_name='rate_percentage', lookup_expr='lt')
    rate_percentage__gt = filters.NumberFilter(field_name='rate_percentage', lookup_expr='gt')

    imdb_rank_percent__lt = filters.NumberFilter(field_name='imdb_rank_percent', lookup_expr='lt')
    imdb_rank_percent__gt = filters.NumberFilter(field_name='imdb_rank_percent', lookup_expr='gt')

    visits__lt = filters.NumberFilter(field_name='visits', lookup_expr='lt')
    visits__gt = filters.NumberFilter(field_name='visits', lookup_expr='gt')

    duration__lt = filters.CharFilter(field_name='duration', lookup_expr='lt')
    duration__gt = filters.CharFilter(field_name='duration', lookup_expr='gt')

    class Meta:
        model = Movie
        fields = [
            'published_at', 'release_year',
            'rate_percentage', 'imdb_rank_percent',
            'duration', 'visits'
        ]


class GenreFilter(filters.FilterSet):
    
    movie_count = filters.NumberFilter(field_name='movie_count')
    movie_count__lt = filters.NumberFilter(field_name='movie_count', lookup_expr='lt')
    movie_count__gt = filters.NumberFilter(field_name='movie_count', lookup_expr='gt')

    class Meta:
        model = Genre
        fields = []