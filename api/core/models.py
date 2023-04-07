from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Movie(BaseModel):
    
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        verbose_name=_("id"),
    )
    short_id = models.CharField(
        max_length=10, 
        unique=True, 
        db_index=True,
        verbose_name=_("short id")
    )
    slug = models.SlugField(verbose_name=_("slug"))
    title_fa = models.CharField(max_length=1000, verbose_name=_('Persian title'))
    title_en = models.CharField(max_length=1000, verbose_name=_('English title'))
    summary = models.CharField(max_length=10000, blank=True, verbose_name=_('summary'))
    published_at = models.DateTimeField(verbose_name=_('published at'))
    release_year = models.SmallIntegerField(null=True, verbose_name=_("release_year"))
    rate_percentage = models.FloatField(null=True, verbose_name=_('rate percentage'))
    imdb_rank_percent = models.FloatField(null=True, verbose_name=_('imdb rank percent'))
    duration = models.CharField(max_length=10, blank=True, verbose_name=_('duration'))
    visits = models.IntegerField(null=True, verbose_name=_('visits'))
    cover_image = models.ImageField(null=True, verbose_name=_('cover image'))
    poster_image = models.ImageField(null=True, verbose_name=_('poster image'))
    genres = models.ManyToManyField(to='Genre', related_name='movies', verbose_name=_('genres'))


    def get_filmnet_link(self):
        return f"https://filmnet.ir/contents/{self.short_id}/{self.slug}/"
    
    def __str__(self) -> str:
        return str(self.short_id + '-' + self.slug)

    class Meta:
        db_table = 'Movie'
        verbose_name = _('movie')
        verbose_name_plural = _('movies') 
        ordering = ['-published_at', ]
        


class Genre(BaseModel):
    
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        verbose_name=_("id"),
    )
    short_id = models.CharField(
        max_length=10, 
        unique=True, 
        db_index=True,
        verbose_name=_("short id")
    )
    slug = models.SlugField(verbose_name=_("slug"))
    title = models.CharField(max_length=1000, verbose_name=_('title'))
    body = models.CharField(max_length=10000, blank=True, verbose_name=_('body'))

    def get_filmnet_link(self):
        return f"https://filmnet.ir/categories/{self.short_id}/{self.slug}"
    
    def get_movie_count(self):
        return self.movies.aggregate(count=models.Count('id'))['count']
    
    def __str__(self) -> str:
        return str(self.short_id + '-' + self.slug)

    class Meta:
        db_table = 'Genre'
        verbose_name = _('genre')
        verbose_name_plural = _('genres') 
