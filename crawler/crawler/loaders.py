from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from crawler.items import MovieItem
from crawler.processors import get_genres, remove_nbsp
from w3lib.html import remove_tags, remove_comments


class MovieLoader(ItemLoader):
    """
    Custom item loader for MovieItem.
    """
    
    default_item_class = MovieItem
    
    # Input processors
    genres_in = get_genres  # Use the get_genres processor for 'genres' field
    summary_in = MapCompose(remove_tags, remove_comments, remove_nbsp)  # Use multiple processors for 'summary' field
    
    # Output processors
    id_out = TakeFirst()
    short_id_out = TakeFirst()
    slug_out = TakeFirst()
    title_fa_out = TakeFirst()
    title_en_out = TakeFirst()
    summary_out = TakeFirst()
    published_at_out = TakeFirst()
    release_year_out = TakeFirst()
    rate_percentage_out = TakeFirst()
    imdb_rank_percent_out = TakeFirst()
    duration_out = TakeFirst()
    visits_out = TakeFirst()
