from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """Model for blogs post."""
    title = models.CharField(max_length=30)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation."""
        return f'{self.text} {self.date_added}'
