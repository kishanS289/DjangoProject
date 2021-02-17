# An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational
# database tables into objects that are more commonly used in application code.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now)  # (auto_now_add=True)
    # if we delete user ,post related to user also deletes
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
