from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.title

