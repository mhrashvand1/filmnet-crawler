from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import argparse

parser = argparse.ArgumentParser(
    prog='filmnet crawler'
)
 
parser.add_argument(
    '-c', '--count',
    type=str,
    dest='film_count',
    default='',
    help='Number of movies to be crawled'
)

args = parser.parse_args()
    
process = CrawlerProcess(get_project_settings())
process.crawl('filmnet', film_count=args.film_count)

process.start()