from django.core.urlresolvers import reverse

from django.db import models


class Foto(models.Model):
	fig_caption = models.TextField()
	img = models.ImageField(upload_to="imagenes")
	img_date = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
        	return reverse('galeria.views.detail', kwargs={'foto_id': self.id})
	
	def __unicode__(self):
		return self.fig_caption

class Comentario(models.Model):
	foto = models.ForeignKey('Foto')
	comentario = models.TextField()
	comment_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.comentario
