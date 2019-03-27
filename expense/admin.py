from django.contrib import admin
from expense.models import Board, Category, Expense

# Register your models here.
admin.site.register(Board)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('board', 'name')
    list_filter = ('board',)
    search_fields = ('name',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    '''Admin View for Expense'''

    list_display = ('title', 'amount', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'category', 'amount')
