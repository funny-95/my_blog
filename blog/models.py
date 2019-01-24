from django.db import models
from model_utils.models import TimeStampedModel


class User(TimeStampedModel):
    name = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)


class Category(TimeStampedModel):
    name = models.CharField(max_length=45, unique=True)


class UserArticle(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField()
