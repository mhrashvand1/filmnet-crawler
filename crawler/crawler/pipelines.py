from scrapy.pipelines.images import ImagesPipeline as BaseImagesPipeline
from itemadapter import ItemAdapter
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.http.request import Request, NO_CALLBACK
from asgiref.sync import sync_to_async
import os
import sys
from datetime import datetime
import django
from django.utils import timezone
from django.core.files import File
from crawler.settings import IMAGES_STORE

join = os.path.join
dirname = os.path.dirname
abspath = os.path.abspath

# Append the path of the 'api' directory to the sys.path
# This allows importing modules from the 'api' directory in the parent directory
sys.path.append(join(dirname(abspath(__file__)), '..', '..', 'api'))

# Set the 'DJANGO_SETTINGS_MODULE' environment variable to the path of the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Call the 'setup()' function of the Django module to set up the Django environment
django.setup()

from django.db import transaction
from core.models import Movie, Genre 


class ImagesPipeline(BaseImagesPipeline):
    """
    Custom ImagesPipeline
    Generates the storage address based on Movie short ID, slug and image type.
    """

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        slug = request.meta['slug']
        short_id = request.meta['short_id']
        image_type = request.meta['image_type']
        return f"{slug + '_' + short_id}/full/{image_type + '-' + image_guid}.jpg"

    def get_media_requests(self, item, info):
        item = ItemAdapter(item)
        urls = item['image_urls']
        slug = item['slug']
        short_id = item['short_id']

        return [
            Request(
                urls[0],
                callback=NO_CALLBACK,
                meta={'slug': slug, 'short_id': short_id, 'image_type': 'cover'}
            ),
            Request(
                urls[1],
                callback=NO_CALLBACK,
                meta={'slug': slug, 'short_id': short_id, 'image_type': 'poster'}
            )
        ]



class DBPipeline:
   
    async def process_item(self, item, spider):
        item = ItemAdapter(item).asdict()
        await sync_to_async(self.insert_data)(item)
        return item

    def insert_data(self, item):
        
        del item['image_urls']
        
        try:
            genres_data = item.pop('genres')
        except KeyError:
            genres_data = []
        
        try:
            images = item.pop('images')
            cover_image_path = images[0]['path']
            poster_image_path = images[1]['path']
        except (KeyError, IndexError):
            cover_image_path = None
            poster_image_path = None

        # Convert published_at to a datetime object
        published_at = datetime.strptime(item['published_at'], '%Y-%m-%dT%H:%M:%S')
        published_at = timezone.make_aware(published_at, timezone.utc)
        item['published_at'] = published_at

        with transaction.atomic():
            
            # Create the genres
            genre_objects = []
            
            for g in genres_data:
                genre_obj, created = Genre.objects.update_or_create(
                    id=g.pop('id'),
                    defaults={**g}
                )
                genre_objects.append(genre_obj)
            
            # Create the Movie
            movie_obj, created = Movie.objects.update_or_create(
                id=item.pop('id'),
                defaults={**item}
            )
            
            # Set the genres for movie
            movie_obj.genres.set(genre_objects)
            
            # Set the cover_image and poster image
            if cover_image_path:
                with open(join(IMAGES_STORE, cover_image_path), 'rb') as f:
                    movie_obj.cover_image.save(cover_image_path, File(f))
            
            if poster_image_path:
                with open(join(IMAGES_STORE, poster_image_path), 'rb') as f:
                    movie_obj.poster_image.save(poster_image_path, File(f))

            movie_obj.save()
