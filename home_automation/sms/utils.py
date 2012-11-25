# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


import requests
from bs4 import BeautifulSoup


MOTION_URL = 'http://localhost:9000'


def extract_readable_string(html):
    soup = BeautifulSoup(html)
    return list(soup.body.descendants)[-1].strip()


def get_motion_status():
    r = requests.get('{0}/0/detection/status'.format(MOTION_URL))
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
