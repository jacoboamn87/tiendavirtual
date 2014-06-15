from django.conf.urls import patterns, include, url

from django.contrib import admin
from oscar.app import application
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls))
]
