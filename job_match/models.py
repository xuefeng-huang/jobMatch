from __future__ import unicode_literals

from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
        
        
class Publication(models.Model):
    link = models.CharField(max_length=500)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.link
