from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.HomeView.as_view(), name='Home'),
	path('nosotros/', views.NosotrosView.as_view(), name='Nosotros'),
	path('contacto/', views.ContactoView.as_view(), name='Contacto'),
	path('arquitectura/', views.ArquiView.as_view(), name='Arquitectura'),
	path('interiorismo/', views.InteriorView.as_view(), name='Interiorismo'),
	path('desarrollo/', views.DesaView.as_view(), name='Desarrollos'),
	path('preventa-inversion/', views.PreView.as_view(), name='Preventa')
	]