from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from absa_app.forms import TextForSentiment

# Create your views here.
base = 'absa_app'

class HomeView(TemplateView):
	template_name = f"{base}/home.html"

	def get(self, request) -> HttpResponse:
		textform = TextForSentiment()
		return render(request, self.template_name, context={'textform': textform})
	
	def post(self, request):
		textform = TextForSentiment(request.POST)
		if textform.is_valid():
			text = textform.cleaned_data['text']
			textform = TextForSentiment()

			args = { 'textform': textform,
		             'value': ' '.join(['Your Text:' ,text]) }

			return render(request, self.template_name, args)

		else:
			return redirect('absa_app:home')
