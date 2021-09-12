from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=200)
    latin_name = models.CharField(max_length=200, default="none")
    status = models.CharField(max_length=200, default="none")
    image_url = models.CharField(max_length=200, default="none")
    description = models.CharField(max_length=10000, default="none")

    def __str__(self):
        return self.name
