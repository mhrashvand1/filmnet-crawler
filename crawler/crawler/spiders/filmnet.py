import scrapy
from crawler.items import MovieItem
from crawler.loaders import MovieLoader
from urllib.parse import parse_qs, urlparse


class FilmnetSpider(scrapy.Spider):
    
    name = "filmnet"
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        # Get the film count
        self.film_count = kwargs.get("film_count", 100)
        # Standard unit of the count per request 
        self.unit = 20


    def start_requests(self):
        
        offset = 0
        for _ in range(self.film_count//self.unit):   
            yield scrapy.Request(
                url=f'https://filmnet.ir/api-v2/video-contents?offset={offset}&count={self.unit}&order=latest&types=single_video',
                callback=self.parse
            )
            offset += self.unit
            
        count = self.film_count % self.unit
        yield scrapy.Request(
            url=f'https://filmnet.ir/api-v2/video-contents?offset={offset}&count={count}&order=latest&types=single_video',
            callback=self.parse
        )


    def parse(self, response):
        
        # Getting the ID of each movie and requesting to get its details
        json_response = response.json()
        for movie in json_response['data']:
            # Get the id
            movie_id = movie['id'].strip()
            # Request to the detail api url
            yield scrapy.Request(
                url=f"https://filmnet.ir/api-v2/video-contents/{movie_id}/",
                callback=self.parse_movie_detail,
            )                
    
    
    def parse_movie_detail(self, response):
        
        # Get the response data
        data = response.json()['data']
        # Instatiate the item loader
        l = MovieLoader(item=MovieItem(), response=response)
        
        l.add_value('id', data['id'])
        l.add_value('short_id', data['short_id'])
        l.add_value('title_fa', data['title'])
        l.add_value('title_en', data['original_name'])
        l.add_value('summary', data['summary'])
        l.add_value('slug', data['slug'])
        l.add_value('published_at', data['published_at'])
        l.add_value('release_year', data['year'])
        l.add_value('rate_percentage', data['rate_percentage'])
        l.add_value('imdb_rank_percent', data['imdb_rank_percent'])
        l.add_value('duration', data['duration'])
        l.add_value('visits', data['visits'])
        l.add_value('genres', data['categories'])  
        # Note that you must add the cover_image before the poster_image
        l.add_value('image_urls', data['cover_image']['path'])
        l.add_value('image_urls', data['poster_image']['path'])
        
        return l.load_item()
     
    
    @staticmethod
    def parse_query_params(url):
        """
        Parse query parameters from a URL and return a dictionary.

        Args:
            url (str): URL containing query parameters.

        Returns:
            dict: A dictionary of parsed query parameters.
        """
        # Parse the URL
        parsed_url = urlparse(url)

        # Get the query parameters from the URL query string
        query_params = parse_qs(parsed_url.query)

        # Convert values to single values instead of lists
        query_params = {key: int(value[0]) if value[0].isdigit() else value[0] for key, value in query_params.items()}

        return query_params