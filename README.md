# filmnet-crawler

## Navigation
- [Run](#run)
  - [Run Django Project](#run-django-project)  
  - [Run Crawler](#run-crawler) 
- [URLs](#urls)


------
## Run

### Run Django Project  

After installing requirements:   
  
``` shell
cd api/ 
./manage.py migrate   
./manage.py runserver  
```

### Run Crawler  
There are 2 ways to run the crawler:   

  
- 1   

``` shell
# In the api/ directory  
./manage.py crawl # -c <number>  
 
```    

- 2   

``` shell   
# In the crawler/ directory 
python go_spider.py # -c <number>

```   

Note that the -c/--count option specifies the count of movies to be crawled (default=100)   

------
## URLs   

### admin panel:
- `admin/`    

### API endpoints:  

- GET movie list:  
`movies/`   

- GET movie detail:  
`movies/<short_id>/`   

- DELETE movie:  
`movies/<short_id>/`    

- DELETE all movies:  
`movies/`    

- GET genre list:   
`genres/`

- GET genre detail:  
`genres/<short_id>/`  

------