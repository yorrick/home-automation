#!/usr/bin/python

import os, re
import sys
import smtplib
import sys
 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
sender = 'yorrick.jansen@gmail.com'
password = "3edcvfrtgb"
recipient = 'yorrick.jansen@gmail.com'
subject = 'Python emaillib Test'
video_name = sys.argv[1]
message = 'Video created'
reg = re.compile(r'''(?P<file_index>\d+)-\d+-\d+\.jpg''')
 
directory = "/tmp/motion/"
 
def main():
    msg = MIMEMultipart()
    msg['Subject'] = 'Python emaillib Test'
    msg['To'] = recipient
    msg['From'] = sender
 
    files = os.listdir(directory)
    # gifsearch = re.compile(".gif", re.IGNORECASE)
    cam_video_search = re.compile(r'''(?P<file_index>\d+)-\d+\.avi''')
    index = cam_video_search.match(video_name).group('file_index')

    cam_image_search = re.compile(r'''{0}-\d+-\d+\.jpg'''.format(index))

    files = filter(cam_image_search.search, files)[:3]
    for filename in files:
        path = os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue
 
        img = MIMEImage(open(path, 'rb').read(), _subtype="jpg")
        img.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(img)
 
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
 
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)
 
    session.sendmail(sender, recipient, msg.as_string())
    session.quit()
 
if __name__ == '__main__':
    main()
