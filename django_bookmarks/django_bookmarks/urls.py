from django.conf.urls import patterns, include, url
from bookmarks.views import *
from django.views.generic.simple import direct_to_template
import os

site_media = os.path.join(os.path.dirname(__file__),'site_media')
print 'site_media = ', site_media
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$',main_page),
    (r'^user/(\w+)/$',user_page),
    
    (r'^login/$','django.contrib.auth.views.login'),
    (r'^logout/$',logout_page),
    (r'^register/$',register_page),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': site_media}),
    
    (r'^register/success/$',direct_to_template,{'template':'registration/register_success.html'}),
    
    (r'^save/$',bookmark_save_page)
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    #url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
