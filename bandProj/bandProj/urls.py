from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.contrib import admin
from views import home, theBand

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bandProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Build Generic URL patterns like this. Add import to the top of this page from views, and create the view.
    # Example link: <a href="\theBand">Meet the Band!</a>
    url(r'^$', home),
	url(r'^theBand', theBand),
)
