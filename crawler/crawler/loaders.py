from itemloaders.processors import MapCompose
from scrapy.loader import ItemLoader
from crawler.items import MovieItem
from crawler.processors import get_genres
from w3lib.html import remove_tags



class MovieLoader(ItemLoader):
    
    default_item_class = MovieItem
    
    genres_in = get_genres
    summary_in = MapCompose(remove_tags)
