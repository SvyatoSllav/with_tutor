from django.urls import path

from . import views

app_name = 'reading'


urlpatterns = [
    path('', views.reading_theme, name='reading_theme'),
    path('reading_subsection/<int:material_theme_id>/', views.reading_subsection, name='reading_subsection'),
    path('reading_material/<int:reading_material_id>/', views.reading_material, name='reading_material' ),
]
