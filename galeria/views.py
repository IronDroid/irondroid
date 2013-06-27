from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from galeria.models import Foto

def index(request):
	f = Foto.objects.all()
	return render_to_response('home.html', {'fotos': f, 'title': 'Mi Galeria'} ,context_instance=RequestContext(request))

def detail(request, foto_id):
	f = Foto.objects.get(id=foto_id)
	return render_to_response('detail.html', {'foto': f, 'title': f.fig_caption} ,context_instance=RequestContext(request))