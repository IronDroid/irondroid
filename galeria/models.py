from django.db import models

class Foto(models.Model):
	fig_caption = models.TextField()
	img = models.ImageField(upload_to="imagenes")
	img_date = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.fig_caption