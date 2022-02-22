from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GrammarMaterial
# Create your views here.

def grammar_materials(request):
    template = 'grammar/grammar_materials.html'
    material = GrammarMaterial.objects.all()
    paginator = Paginator(material, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Грамматика'
    }
    return render(request, template, context)
