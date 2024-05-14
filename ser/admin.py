from django.contrib import admin

# Register your models here.
from .models import Category, Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ["id","text","author"]

    class Meta:
        model = Quote

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Category)