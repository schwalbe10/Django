from django.db import models

class Record(models.Model):
    album = models.CharField(u'Jazz Album', max_length=255)
    artist = models.CharField(u'Artist', max_length=255, blank=True)
    year = models.IntegerField(u'Year', max_length=4, blank=True)
    
    def __str__(self):    # Python2: def __unicode__(self):
        return self.album
    
class Review(models.Model):
    record = models.ForeignKey(Record, verbose_name=u'Album', related_name='reviews')
    comment = models.TextField(u'Comment', blank=True)
    
    def __str__(self):    # Python2: def __unicode__(self):
        return self.comment