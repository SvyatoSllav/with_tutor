from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.core.paginator import Paginator
from .models import GrammarMaterial, GrammarTheme, GrammarSubsections


def grammar_theme(request):
    template = 'grammar/grammar_theme.html'
    material = GrammarTheme.objects.all()
    paginator = Paginator(material, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Грамматика',
    }
    return render(request, template, context)

def grammar_subsection(request, material_theme_id):
    template = 'grammar/material_subsection.html'
    theme = get_object_or_404(GrammarTheme, id=material_theme_id)
    subsections = get_list_or_404(GrammarSubsections, theme=theme)
    materials = [material for material in GrammarMaterial.objects.filter(subsection=subsections[0])]
    paginator = Paginator(subsections, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': theme.title,
        'materials': materials,
        'page_obj': page_obj
    }
    return render(request, template, context)

def grammar_material(request, grammar_material_id):
    template='grammar/grammar_material.html'
    material = get_object_or_404(GrammarMaterial, id=grammar_material_id)
    context = {
        'title': 'random_material',
        'material': material,
    }
    return render(request, template, context)
