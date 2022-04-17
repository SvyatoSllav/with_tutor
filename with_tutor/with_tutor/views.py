from django.views.generic import TemplateView


class MainMenu(TemplateView):
    template_name = 'main-menu/main-menu.html'
