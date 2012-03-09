from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('fcgi_demo.web.views',
    url(r'^$', 'hello', name='hello'),
)

