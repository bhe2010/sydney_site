from django.db import models

# Create your models here.

class Page(models.Model):
    #title of page
    title = models.CharField(max_length=60)
    #permalink to individual page, unique makes sure errors
    #are thrown if permalinks are accidentally duplicated
    permalink = models.CharField(max_length=12, unique=True)
    #date page was last edited
    update_date = models.DateTimeField('Last Updated')
    #html content of the page
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self): #allows us to see the title on admin page
        return self.title