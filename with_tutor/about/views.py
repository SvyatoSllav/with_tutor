from django.views.generic.base import TemplateView


class HomepageStaticPage(TemplateView):
    template_name = 'about/index.html'
