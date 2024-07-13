from django.contrib import admin
from .models import dish_search

class SearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'cordinates')
    search_fields = ('name', 'location', 'items', 'full_details')
    list_filter = ('location',)

admin.site.register(dish_search, SearchAdmin)
