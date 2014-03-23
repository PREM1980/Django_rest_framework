from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    url = models.URLField(unique=True)
    def __unicode__(self):
        return self.url
    
    
class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)
    def __unicode__(self):
        return u'%s, %s %s' % (self.user.username, self.link.url, self.title)
    
    def get_absolute_url(self):
        return self.link.url    
    
class Tag(models.Model):
    name = models.CharField(max_length=64,unique=True)
    bookmarks = models.ManyToManyField(Bookmark)
    def __unicode__(self):
        return self.name

class SharedBookmark(models.Model):
    bookmark = models.ForeignKey(Bookmark, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=1)
    users_voted = models.ManyToManyField(User)

    def __unicode__(self):
        return u'%s, %s' % (self.bookmark, self.votes)
    
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    #reporter = models.ForeignKey(Reporter)
    reporter = models.ForeignKey(Reporter)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)


    

