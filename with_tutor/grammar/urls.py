from django.urls import path

from . import views

app_name = 'grammar'


urlpatterns = [
    path('', views.grammar_materials, name='grammar'),
    path('grammar_detail/<int:material_id>/', views.grammar_detail, name='grammar_detail')
]
