from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import argparse

parser = argparse.ArgumentParser(
    prog='filmnet crawler'
)

# Custom validator function to check if the value is a positive integer
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is not a positive integer" % value)
    return ivalue

parser.add_argument(
    '-c', '--count',
    type=positive_int,
    dest='film_count',
    default=100,
    help='Number of movies to be crawled'
)

args = parser.parse_args()
    
process = CrawlerProcess(get_project_settings())
process.crawl('filmnet', film_count=args.film_count)

process.start()