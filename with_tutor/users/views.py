from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('about:index')
    template_name = 'users/signup.html'
