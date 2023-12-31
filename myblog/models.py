from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Feedback(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=60)
    feedback = models.TextField(default='')
    raiting = models.PositiveIntegerField()

class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.SlugField()
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='media_post')
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text