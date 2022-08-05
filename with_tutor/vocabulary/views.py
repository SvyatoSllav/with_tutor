from django.shortcuts import render
from django.core.paginator import Paginator
from .models import VocabularyMaterial


def vocabulary_materials(request):
    template = 'vocabulary/vocabulary_materials.html'
    material = VocabularyMaterial.objects.all().order_by('id')
    paginator = Paginator(material, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Лексика'
    }
    return render(request, template, context)

def vocabulary_detail(request, material_id):
    template = 'material_detail.html'
    material = VocabularyMaterial.objects.get(pk=material_id)
    context = {
        'material': material
    }
    return render(request, template, context)
