from django.shortcuts import render
from .models import ReadingMaterial
from django.core.paginator import Paginator
# Create your views here.

def reading_materials(request):
    template='reading/reading_index.html'
    materials = ReadingMaterial.objects.all()
    paginator = Paginator(materials, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = 'Чтение'
    context = {
        'title': title,
        'page_obj': page_obj
    }
    return render(request, template, context)
