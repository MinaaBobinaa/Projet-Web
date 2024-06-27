from django.contrib import admin
from .models import House

# Register your models here.
#admin.site.register(House)

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'location', 'price')
    list_filter = ('type',)  # Add a filter sidebar for house types