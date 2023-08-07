from django.db import models


class AboutPage(models.Model):

    title = models.CharField(max_length=80, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title
