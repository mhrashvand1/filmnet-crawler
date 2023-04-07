from django.contrib import admin
from core.models import Movie, Genre


admin.site.register(Movie, admin.ModelAdmin)  
admin.site.register(Genre, admin.ModelAdmin)  