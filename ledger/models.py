from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


# Create your models here.
class Project(models.Model):
    name = forms.CharField('Name', max_length=100, required=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Transaction(models.Model):
    """
    Transactions model
    It  manages the transactions of company to different users
    """
    pass
