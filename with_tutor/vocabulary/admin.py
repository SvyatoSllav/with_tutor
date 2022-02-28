from django.contrib import admin
from .models import VocabularyMaterial
# Register your models here.

class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(VocabularyMaterial, VocabularyAdmin)
