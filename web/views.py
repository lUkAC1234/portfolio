from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import ContactModel, ProjectsModel
from .forms import ContactForm
from django.urls import reverse_lazy

class index(CreateView):
    form_class = ContactForm
    model = ContactModel
    template_name = "pages/index.html"
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['projects'] = ProjectsModel.objects.all()[:6]
        return data

class ProjectsView(ListView):
    model = ProjectsModel
    template_name = "pages/project.html"
