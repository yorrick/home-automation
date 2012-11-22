from django.conf.urls import url, patterns

urlpatterns = patterns('twilio_test.sms.views',
    url(r'^receive/$', 'receive', name='receive'),
    url(r'^answer/$', 'answer', name='answer'),
)
