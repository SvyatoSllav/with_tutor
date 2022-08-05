from django.contrib import admin
from .models import ReadingTheme, ReadingSubsections, ReadingMaterial

class ReadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date')
    empty_value_display = '-пусто-'


class ReadingSubsectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date')
    empty_value_display = '-пусто-'


class ReadingMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')
    empty_value_display = '-пусто-'

admin.site.register(ReadingTheme, ReadingAdmin)
admin.site.register(ReadingSubsections, ReadingSubsectionsAdmin)
admin.site.register(ReadingMaterial, ReadingMaterialAdmin)