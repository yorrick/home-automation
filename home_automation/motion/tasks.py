# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

import os, re
import smtplib

from email.mime.image import MIMEImage
from email.MIMEBase import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
from django_ztask.decorators import task
from django.conf import settings

logger = logging.getLogger(__name__)


#@task()
#def print_this(msg):
#    logger.info(msg)


@task()
def send_email(video_id):
    logger.info('Trying to send email for video {0!r}'.format(video_id))

    msg = MIMEMultipart()
    msg['Subject'] = 'Motion detected'
    msg['To'] = settings.MAIL_RECIPIENT
    msg['From'] = settings.MAIL_SERVER_LOGIN

    files = os.listdir(settings.MOTION_DIRECTORY)
    cam_video_search = re.compile(r'''(?P<file_index>\d+)-\d+\.avi''')

    cam_video_match = cam_video_search.match(video_id)
    if cam_video_match is None:
        logger.warn('Could not find video {0!r}'.format(video_id))
        return

    index = cam_video_match.group('file_index')

    cam_image_search = re.compile(r'''{0}-\d+-\d+\.jpg'''.format(index))

    files = filter(cam_image_search.search, files)[:settings.MAIL_PICTURE_NUMBER]
    logger.info('Attaching pictures')
    for filename in files:
        logger.info('Attaching picture {0}'.format(filename))

        path = os.path.join(settings.MOTION_DIRECTORY, filename)
        if not os.path.isfile(path):
            continue

        img = MIMEImage(open(path, 'rb').read(), _subtype="jpg")
        img.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(img)

    if settings.MAIL_SEND_VIDEO:
        logger.info('Attaching video')
        part = MIMEBase('application', "octet-stream")
        video_path = os.path.join(settings.MOTION_DIRECTORY, video_id)
        fo = open(video_path, "rb")
        part.set_payload(fo.read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'\
            .format(os.path.basename(video_id)))
        msg.attach(part)

    logger.info('Attaching text')
    part = MIMEText('text', "plain", 'utf-8')
    part.set_payload('Motion has been detected')
    msg.attach(part)

    logger.info('Opening session on {0}:{1}'.format(settings.MAIL_SERVER_HOST, settings.MAIL_SERVER_PORT))
    session = smtplib.SMTP(settings.MAIL_SERVER_HOST, settings.MAIL_SERVER_PORT)

    logger.info('Starting TLS')
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(settings.MAIL_SERVER_LOGIN, settings.MAIL_SERVER_PASSWORD)

    logger.info('Sending email for video {0!r}....'.format(video_id))

    session.sendmail(settings.MAIL_SERVER_LOGIN, settings.MAIL_RECIPIENT, msg.as_string())
    session.quit()

    logger.info('Done: send email for video {0!r}'.format(video_id))
