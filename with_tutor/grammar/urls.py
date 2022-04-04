from django.urls import path

from . import views

app_name = 'grammar'


urlpatterns = [
    path('', views.grammar_theme, name='grammar'),
    path('grammar_subsection/<int:material_theme_id>/', views.grammar_subsection, name='grammar_subsection'),
    path('grammar_material/<int:grammar_material_id>/', views.grammar_material, name='grammar_material' ),
]
