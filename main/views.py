from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

class PresentView(View):
    
    def get(self, request):
        template_name = "presentacion.html"
        return render(request, template_name)

class HomeView(View):

    def get(self, request):
        template_name = "index.html"
        return render(request, template_name)

class NosotrosView(View):
    
    def get(self, request):
        template_name = "nosotros.html"
        return render(request, template_name)

class ContactoView(View):
    
    def get(self, request):
        template_name = "contacto.html"
        return render(request, template_name)

class ArquiView(View):
    
    def get(self, request):
        template_name = "arquitectura.html"
        return render(request, template_name)

class InteriorView(View):
    
    def get(self, request):
        template_name = "interiorismo.html"
        return render(request, template_name)

class DesaView(View):
    
    def get(self, request):
        template_name = "desarrollo.html"
        return render(request, template_name)

class PreView(View):
    
    def get(self, request):
        template_name = "preventa.html"
        return render(request, template_name)