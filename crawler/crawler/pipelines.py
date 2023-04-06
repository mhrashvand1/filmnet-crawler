from scrapy.pipelines.images import ImagesPipeline as BaseImagesPipeline
from itemadapter import ItemAdapter
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.http.request import Request, NO_CALLBACK
from asgiref.sync import sync_to_async


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
        urls = item['image_urls']
        movie_id = item['id'][0]
    
        return [
            Request(
                urls[0],
                callback=NO_CALLBACK, 
                meta={'movie_id':movie_id, 'image_type':'cover'}       
            ),
            Request(
                urls[1],
                callback=NO_CALLBACK, 
                meta={'movie_id':movie_id, 'image_type':'poster'}       
            )
        ]


class DBPipeline: 
   
    async def process_item(self, item, spider):
        item = ItemAdapter(item).asdict()  
        try:
            await sync_to_async(self.insert_data)(item)  
        except:
            pass
        return item


    def insert_data(self, item):
        # print("\n\n", item, "\n\n")
        pass
        # with transaction.atomic():
        #     page = Page.objects.get(username=item.get('username'))
        #     source_created = datetime.strptime(
        #         item.get("source_created"),
        #         "%Y-%m-%d %H:%M:%S"
        #     )
        #     post, created = Post.objects.get_or_create(
        #         page=page, 
        #         source_id=item.get('source_id'),
        #         title=item.get('title'),
        #         text=item.get('text'),
        #         source_created=source_created
        #     )
        #     if created:
        #         # Create main media
        #         main_media_url = item.get("media").get("main_media")
        #         Media.objects.create(post=post, url=main_media_url, is_main=True)
        #         # Create other media
        #         other_media_urls = item.get("media").get("other_media")
        #         data = [Media(post=post, url=url) for url in other_media_urls]
        #         Media.objects.bulk_create(data)
                
        #     print(f"\n Post {item.get('source_id')} created successfullt. \n")
        