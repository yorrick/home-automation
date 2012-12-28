from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home_automation.views.home', name='home'),
    # url(r'^home_automation/', include('home_automation.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
    url(r'^sms/', include('home_automation.sms.urls', namespace='sms')),
    url(r'^motion/', include('home_automation.motion.urls', namespace='motion')),
)
