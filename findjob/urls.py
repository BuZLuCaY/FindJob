from django.conf.urls import patterns, include, url
from management import views
from django.contrib.auth.views import login
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'findjob.views.home', name='home'),
    # url(r'^findjob/', include('findjob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',views.index, name='mainPage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$',views.profile, name='myProfile'),
    url(r'^postJob/$',views.postJob, name='postJob'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'base.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^google/$',views.google,name='google'),
    url(r'^search/$',views.search,name='search'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^profile/profile_pictures/(.*)',views.profile_pictures),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()