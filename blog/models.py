from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model): #Post is an object and Django model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link to another model
    title = models.CharField(max_length=200) #text with limited num of characters
    text = models.TextField() #long text with limited num of characters
    created_date = models.DateTimeField(default=timezone.now) #data and time
    published_date = models.DateTimeField(blank=True, null=True) #data and time

    def publish(self):#method to publish posts
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
