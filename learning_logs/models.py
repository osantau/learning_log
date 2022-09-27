from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific learnd about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
