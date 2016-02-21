from django.contrib import admin
from cms.models import Record, Review

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'artist', 'year',)  # Displayed items in the list
    list_display_links = ('id', 'album',)  # Items with the link to edit them
admin.site.register(Record, RecordAdmin)
 
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)  # Displayed items in the list
    list_display_links = ('id', 'comment',)  # Items with the link to edit them
admin.site.register(Review, ReviewAdmin)