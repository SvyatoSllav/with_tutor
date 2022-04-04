from django.urls import path

from . import views

app_name = 'reading'


urlpatterns = [
    path('', views.reading_materials, name='reading_materials'),
]
