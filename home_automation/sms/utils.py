# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import requests
import logging
from bs4 import BeautifulSoup

from django.conf import settings
from requests import ConnectionError


logger = logging.getLogger(__name__)


def extract_readable_string(html):
    soup = BeautifulSoup(html)
    return list(soup.body.descendants)[-1].strip()


def get_motion_status():
    try:
        r = requests.get('{0}/0/detection/status'.format(settings.MOTION_URL))
    except ConnectionError as e:
        logger.warn('Could not reach motion')
        return 'STOPPED'

    return extract_readable_string(r.content)


#r = requests.get('http://localhost:8080/0/detection/status')
#print extract_readable_string(r.content)
#
#r = requests.get('http://localhost:8080/0/detection/start')
#print extract_readable_string(r.content)
#
#r = requests.get('http://localhost:8080/0/detection/pause')
#print extract_readable_string(r.content)
#
