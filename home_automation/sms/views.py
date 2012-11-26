# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from django.http import HttpResponseNotFound
from django_twilio.decorators import twilio_view
from django.conf import settings

from twilio.twiml import Response

from home_automation.sms.utils import get_motion_status


logger = logging.getLogger(__name__)


callers = {
    "+15146258937": "Peanut",
}


@twilio_view
def receive(request):
    logger.debug('Get params: {0}'.format(request.GET))
    logger.debug('Post params: {0}'.format(request.POST))

#    {
#     u'Body': [u'Helo toto'],
#     u'FromZip': [u''],
#     u'SmsStatus': [u'received'],
#     u'FromCountry': [u'CA'],
#     u'FromCity': [u'MONTREAL'],
#     u'ApiVersion': [u'2010-04-01'],
#     u'To': [u'+15144180546'],
#     u'From': [u'+15146258937'],
#     u'ToZip': [u''],
#     u'ToCountry': [u'CA'],
#     u'ToState': [u'QC'],
#     u'AccountSid': [u'AC791403f3ec0098401e629d6aaf6b44bd'],
#     u'SmsSid': [u'SMb928abbc11c19f6e9f5215ec15e151c8'],
#     u'ToCity': [u'MONTREAL'],
#     u'FromState': [u'QC'],
#     u'SmsMessageSid': [u'SMb928abbc11c19f6e9f5215ec15e151c8']
#    }

    from_number = request.POST.get('From', None)
    if from_number in callers:
        r = Response()
        r.sms('Voici ton message, peanut! ({0})'.format(request.POST.get('Body', '')))
        return r
    else:
        return HttpResponseNotFound('Could not find your stuff')


@twilio_view
def status(request):
    logger.debug('Get params: {0}'.format(request.GET))
    logger.debug('Post params: {0}'.format(request.POST))

    from_number = request.POST.get('From', None)

    if not settings.DEBUG and from_number not in callers:
        return HttpResponseNotFound('Could not find your stuff')

    logger.debug('getting motion status')
    status = get_motion_status()
    logger.debug('got motion status: {0}'.format(status))
    r = Response()
    r.sms('Status for motion: {0}'.format(status))
    return r


@twilio_view
def answer(request):
    logger.debug('Get params: {0}'.format(request.GET))
    logger.debug('Post params: {0}'.format(request.POST))

    from_number = request.POST.get('From', None)
    if from_number in callers:
        resp = Response()
        resp.say("Hello peanut")
        return str(resp)
    else:
        return HttpResponseNotFound()

