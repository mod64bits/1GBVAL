from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Slider, About


class HomeView(TemplateView):
    template_name = "home/home.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Slider.objects.all()
        context["sobre"] = About.objects.filter()
        
        return context
