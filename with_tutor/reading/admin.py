from django.contrib import admin
from .models import ReadingMaterial
# Register your models here.

class ReadingMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(ReadingMaterial, ReadingMaterialAdmin)
