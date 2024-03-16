from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
base = 'absa_app'

class HomeView(TemplateView):
	template_name = f"{base}/home.html"
