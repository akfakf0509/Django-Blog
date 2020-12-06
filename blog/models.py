from django.db import models


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey('Post', related_name='post', on_delete=models.CASCADE, db_column='post_id')
    date = models.DateTimeField('date published')
    content = models.CharField(max_length=200)
    likes = models.IntegerField()
