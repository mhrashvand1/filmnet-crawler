from scrapy.pipelines.images import ImagesPipeline as BaseImagesPipeline
from itemadapter import ItemAdapter
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.http.request import Request, NO_CALLBACK
from contextlib import suppress


class ImagesPipeline(BaseImagesPipeline):
    
    """
    Custom ImagesPipeline
        Generate the storage address based on Movie ID and image type
    """
    
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        movie_id, image_type = request.meta['movie_id'], request.meta['image_type']
        return f"{movie_id}/full/{image_type+image_guid}.jpg"

    def get_media_requests(self, item, info):
        item = ItemAdapter(item)
        movie_id = item.get('id')
        return [
            Request(
                item.get('cover_image_url'),
                callback=NO_CALLBACK, 
                meta={'movie_id':movie_id, 'image_type':'cover'}
            ),
            Request(
                item.get('poster_image_url'),
                callback=NO_CALLBACK, 
                meta={'movie_id':movie_id, 'image_type':'poster'}
            ),   
        ]

    def item_completed(self, results, item, info):
        with suppress(KeyError):
            ItemAdapter(item)['cover_image'] = results[0]
            ItemAdapter(item)['poster_image'] = results[1]
        return item


class DBPipeline: 
    def process_item(self, item, spider):
        return item
