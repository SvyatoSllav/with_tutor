from django.contrib import admin
from .models import GrammarMaterial
# Register your models here.

class GrammarAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(GrammarMaterial, GrammarAdmin)