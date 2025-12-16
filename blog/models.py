from django.db import models
# we need to import the user tables
from django.conf import settings
from django.utils import timezone

# Create your models here.
# db blog columns
# author - user who made the post
# title - title of post
# text - body of post
# created_date - when post was made
# published_date - when post was approved or published

# make a class called blog post or post for short, and add the columns
# https://docs.djangoproject.com/en/5.2/ref/models/fields/
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text