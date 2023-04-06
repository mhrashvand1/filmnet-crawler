import scrapy


class MovieItem(scrapy.Item):
    
    id = scrapy.Field()
    short_id = scrapy.Field()
    slug = scrapy.Field()
    fa_title = scrapy.Field()
    en_title = scrapy.Field()
    summary = scrapy.Field()
    publish_date = scrapy.Field()
    release_year = scrapy.Field()
    rate = scrapy.Field()
    duration = scrapy.Field()
    
    # The url of the cover and poster image in the filmnet
    cover_image_url = scrapy.Field()
    poster_image_url = scrapy.Field()
    
    # The url of the downloaded poster and cover image
    cover_image = scrapy.Field()
    poster_image = scrapy.Field()
    
    # List of the genres
    genres = scrapy.Field()
    
    # filmnet_link: This field is a combination of slug and short_id and does not need to be taken separately, 
    # but this field is created in the serializer that is used to display the movie in the Django project.