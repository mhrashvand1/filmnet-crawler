from rest_framework import serializers
from core.models import Movie, Genre


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Genre model."""
        
    movie_count = serializers.ReadOnlyField(source='get_movie_count')
    filmnet_link = serializers.ReadOnlyField(source='get_filmnet_link')
        
    class Meta:
        model = Genre
        fields = [
            'id', 'short_id', 'slug', 'title', 
            'body', 'movie_count', 'filmnet_link'
        ]


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Movie model."""
    
    genres = GenreSerializer(many=True)
    filmnet_link = serializers.ReadOnlyField(source='get_filmnet_link')

    class Meta:
        model = Movie
        fields = [
            'id', 'short_id', 'slug', 'title_fa', 'title_en',
            'release_year', 'duration', 'cover_image', 'poster_image',
            'summary', 'genres', 'visits', 'rate_percentage', 'imdb_rank_percent',
            'published_at', 'filmnet_link'
        ]
