# -*-coding: utf-8 -*-

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Katip(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=50)
    flag = models.CharField(max_length=2)
    priority = models.CharField(max_length=2)
    pubtime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)
    
    class Meta:
        ordering = ['priority', 'pubtime']


