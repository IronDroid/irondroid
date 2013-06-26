from django.contrib import admin
from galeria.models import Foto, Comentario

class FotoAdmin(admin.ModelAdmin):
	fields = ['img', 'fig_caption']

admin.site.register(Foto, FotoAdmin)
admin.site.register(Comentario)