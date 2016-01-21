from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default
import datetime

class Article(models.Model):
    def __str__(self):
        return self.title
        
    title = models.CharField(max_length=50)
    content = models.TextField()
   
class Comment(models.Model):
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, related_name='article')