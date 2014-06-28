
import urllib2
import os
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64

with open('../app.txt','r') as fid:
    userinfo = fid.readlines()
    userinfo = [u.strip() for u in userinfo]

def sendMail(subject, text, *attachmentFilePaths):
    gmailUser = userinfo[0]
    gmailPassword = userinfo[1]
    recipient = userinfo[0]
    msg = MIMEMultipart()
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    for attachmentFilePath in attachmentFilePaths:
      msg.attach(getAttachment(attachmentFilePath))
    
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    
    print('Sent email to %s' % recipient)


def getAttachment(attachmentFilePath):

    contentType, encoding = mimetypes.guess_type(attachmentFilePath)
    
    if contentType is None or encoding is not None:
      contentType = 'application/octet-stream'
    
    mainType, subType = contentType.split('/', 1)
    
    file = open(attachmentFilePath, 'rb')
    
    if mainType == 'text':
      attachment = MIMEText(file.read())
    elif mainType == 'message':
      attachment = email.message_from_file(file)
    elif mainType == 'image':
      attachment = MIMEImage(file.read(),_subType=subType)
    elif mainType == 'audio':
      attachment = MIMEAudio(file.read(),_subType=subType)
    else:
      attachment = MIMEBase(mainType, subType)
    
    attachment.set_payload(file.read())
    encode_base64(attachment)
    
    file.close()
    
    attachment.add_header('Content-Disposition', 'attachment',   filename=os.path.basename(attachmentFilePath))
    
    return attachment

#fqn = os.uname()[1]

def email_ip_addr():
    ext_ip = urllib2.urlopen('http://icanhazip.com').read()
    sendMail('IP', ext_ip)


# s=smtplib.SMTP()
# s.connect("smtp.gmail.com",465)
# s.ehlo()
# s.starttls()
# s.login("wolf809@gmail.com", "043v0lut10n")
# s.sendmail("wolf809@gmail.com", "wolf809@gmail.com", ext_ip)

# mail('wolf809@gmail.com', ext_ip)
