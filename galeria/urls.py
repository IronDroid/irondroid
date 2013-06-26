from django.conf.urls import patterns, include, url

urlpatterns = patterns('galeria.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<foto_id>\d+)/$', 'detail', name='detail'),
)