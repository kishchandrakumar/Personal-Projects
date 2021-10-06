from django.shortcuts import render

# from django.http import HttpResponse
from django.views.generic import TemplateView


# def homePageView(request): 
#     '''
#     A function to respond to HTTP requests
#     '''
#     return HttpResponse('Hello World!')

class HomePageView(TemplateView): #Inherited all required logic
    template_name = 'home.html'   # References template created in project level directory

class AboutPageView(TemplateView):
    template_name = 'about.html'