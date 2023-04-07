from django.core.management.base import BaseCommand, CommandError
import os
import sys


class Command(BaseCommand):

    help = 'crawl command'

    def add_arguments(self, parser):
        parser.add_argument(
            '-c', 
            '--count', 
            type=int,
            help='Number of movies to be crawled (default=100)',
            default=100
        )


    def handle(self, *args, **kwargs):        
        count = kwargs['count']

        if count <= 0:
            raise CommandError('The count argument must be a positive integer.')
        
        self.run_crawler(count=count)
        self.stdout.write(self.style.SUCCESS(f'Successfully crawled items.'))

    
    @staticmethod
    def run_crawler(count=100):
        executable = sys.executable
        command = f"cd ../crawler/ && {executable} go_spider.py -c {count}"
        os.system(command)