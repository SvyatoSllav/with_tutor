from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.core.paginator import Paginator
from .models import ReadingTheme, ReadingMaterial,  ReadingSubsections
from django.shortcuts import HttpResponse


def reading_theme(request):
    template = 'reading/reading_theme.html'
    material = ReadingTheme.objects.all()
    paginator = Paginator(material, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Лексика',
    }
    return render(request, template, context)


def reading_subsection(request, material_theme_id):
    template = 'reading/reading_subsection.html'
    theme = get_object_or_404(ReadingTheme, id=material_theme_id)
    subsections = get_list_or_404(ReadingSubsections, theme=theme)
    materials = [material for material in ReadingMaterial.objects.filter(subsection=subsections[0])]
    context = {
        'title': theme.title,
        'subsections': subsections,
        'materials': materials
    }
    return render(request, template, context)

def reading_material(request, reading_material_id):
    template='reading/reading_material.html'
    material = get_object_or_404(ReadingMaterial, id=reading_material_id)
    context = {
        'title': 'random_material',
        'material': material
    }
    return render(request, template, context)
