# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from django.http import HttpResponse
from home_automation.motion.tasks import print_this


logger = logging.getLogger(__name__)


def motion_detected(request, picture_id):
    msg = 'Motion detected with picture id {0}'.format(picture_id)
    logger.info(msg)
    print_this.async(msg)
    return HttpResponse('Done')