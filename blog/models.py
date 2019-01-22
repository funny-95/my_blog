from django.db import models
from model_utils.models import TimeStampedModel


class User(TimeStampedModel):
    name = models.CharField(max_field=45, unique=True)
    password = models.CharField(max_field=255)


class Category(TimeStampedModel):
    name = models.CharField(max_field=45, unique=True)


class Theme(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_field=45, unique=True)


class Article(TimeStampedModel):
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField()
