from django.contrib import admin
from ledger.models import Board, Category, Transaction

# Register your models here.
admin.site.register(Board)
admin.site.register(Category)
admin.site.register(Transaction)