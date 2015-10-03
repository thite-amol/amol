from django.contrib import admin
from models import Publisher, Author, Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city','state_province','country','website')
    list_filter = ('name',)
    ordering = ('name',)

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
