from django.conf.urls import url, patterns

urlpatterns = patterns('home_automation.motion.views',
    url(r'^motion-detected/(?P<picture_id>\d+)/$', 'motion_detected', name='motion-detected'),
)
