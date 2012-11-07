from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^bbs$', 'bbs.views.index'),
    url(r'^register$', 'bbs.views.register'),
    url(r'^read/(?P<parm>\d{1,})/$', 'bbs.views.read'),
    url(r'^replay/(?P<parm1>\d{1,})$', 'bbs.views.replay'),
    url(r'^replay/(?P<parm3>\d{1,})/(?P<parm2>\d{1,})/$', 'bbs.views.reply'),
    url(r'^login/$', 'bbs.views.login'),
    url(r'^logout/$', 'bbs.views.logout'),
    url(r'^write/$', 'bbs.views.write'),
    # url(r'^$', 'BBS.views.home', name='home'),
    # url(r'^BBS/', include('BBS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
