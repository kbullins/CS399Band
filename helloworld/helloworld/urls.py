from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', url(r'^$', 'helloworld.views.home', name='home'),
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
