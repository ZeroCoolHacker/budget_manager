from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.
class Board(models.Model):
    name = models.CharField('Name', max_length=100, blank=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Category(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name  = models.CharField(max_length=50, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Expense(models.Model):
    """
    Transactions model
    It  manages the transactions of company to different users
    """
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_date = models.DateField('Transaction Date', default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title