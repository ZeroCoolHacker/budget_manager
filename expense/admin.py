from django.contrib import admin
from ledger.models import Board, Category, Transaction

# Register your models here.
admin.site.register(Board)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('board', 'name')
    list_filter = ('board',)
    search_fields = ('name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    '''Admin View for Transaction'''

    list_display = ('title', 'amount', 'category', 'transaction_type')
    list_filter = ('category', 'transaction_type')
    search_fields = ('title', 'category', 'amount')
