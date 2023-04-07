import scrapy


class MovieItem(scrapy.Item):
    # Fields representing movie data
    id = scrapy.Field()
    short_id = scrapy.Field()
    slug = scrapy.Field()
    title_fa = scrapy.Field()
    title_en = scrapy.Field()
    summary = scrapy.Field()
    published_at = scrapy.Field()
    release_year = scrapy.Field()
    rate_percentage = scrapy.Field()
    imdb_rank_percent = scrapy.Field()
    duration = scrapy.Field()
    visits = scrapy.Field()
    
    # Fields for movie images
    # The URL of the cover and poster image in the filmnet
    image_urls = scrapy.Field()
    # The URL of the downloaded poster and cover image
    images = scrapy.Field()
    
    # Field for movie genres
    # List of genres
    genres = scrapy.Field()
    
    # Additional notes on fields
    # filmnet_link: This field is a combination of slug and short_id and does not need to be taken separately,
    # but this field is created in the serializer that is used to display the movie in the Django project.
