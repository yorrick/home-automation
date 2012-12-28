# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from django.http import HttpResponse
from home_automation.motion.tasks import send_email


logger = logging.getLogger(__name__)


def motion_detected(request, video_id):
    send_email.async(video_id)
    return HttpResponse('Done')