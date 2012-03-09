from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', redirect_to, { 'url':'/web' }),
    url(r'^web/', include('fcgi_demo.web.urls')),
    # Examples:
    # url(r'^$', 'fcgi_demo.views.home', name='home'),
    # url(r'^fcgi_demo/', include('fcgi_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
