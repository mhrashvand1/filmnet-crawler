from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from crawler.items import MovieItem
from crawler.processors import get_genres
from w3lib.html import remove_tags



class MovieLoader(ItemLoader):
    
    default_item_class = MovieItem
    
    # Input processors
    genres_in = get_genres
    summary_in = MapCompose(remove_tags)
    
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