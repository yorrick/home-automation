from django.conf.urls import url, patterns

urlpatterns = patterns('home_automation.motion.views',
    url(r'^motion-detected/(?P<video_id>[^/]+)/$', 'motion_detected', name='motion-detected'),
)
