from django.conf.urls import patterns, include, url

urlpatterns = patterns('galeria.views',
    url(r'^$', 'index', name='index'),
)