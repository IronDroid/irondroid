from django.shortcuts import render_to_response
from django.template import RequestContext
from galeria.models import Foto

def index(request):
	f = Foto.objects.all()
	return render_to_response('home.html', {'fotos': f},context_instance=RequestContext(request))