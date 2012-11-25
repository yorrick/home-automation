from django.conf.urls import url, patterns

urlpatterns = patterns('home_automation.sms.views',
    url(r'^receive/$', 'receive', name='receive'),
    url(r'^answer/$', 'answer', name='answer'),
    url(r'^motion/status/$', 'status', name='status'),
)
