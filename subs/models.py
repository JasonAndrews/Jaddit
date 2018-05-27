from django.contrib.auth.models import Permission, User
from django.db import models


# subreddit
class Sub(models.Model):
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    submission_text = models.CharField(max_length=1024)

    def __str__(self):
        return self.name + ' - ' + self.title


# thread
class Thread(models.Model):
    sub = models.ForeignKey(Sub, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.sub.name + '/' + self.title


# comment
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.thread.title + '/' + self.id