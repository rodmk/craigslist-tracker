import smtplib
from email.mime.text import MIMEText

class MailSender(object):
  def __init__(
    self,
    smtphost='localhost',
    mailfrom='scrapy@localhost',
    smtpuser=None,
    smtppass=None,
    smtpport=25,
    smtptls=False,
    smtpssl=False,
    debug=False,
  ):
    self.smtphost = smtphost
    self.smtpport = smtpport
    self.smtpuser = smtpuser
    self.smtppass = smtppass
    self.smtptls = smtptls
    self.smtpssl = smtpssl
    self.mailfrom = mailfrom
    self.debug = debug

    self.smtp = smtplib.SMTP_SSL(self.smtphost, self.smtpport)
    self.smtp.login(self.smtpuser, self.smtppass)

  @classmethod
  def from_settings(cls, settings):
    return cls(
      settings['MAIL_HOST'],
      settings['MAIL_FROM'],
      settings['MAIL_USER'],
      settings['MAIL_PASS'],
      settings.getint('MAIL_PORT'),
      settings.getbool('MAIL_TLS'),
      settings.getbool('MAIL_SSL')
    )

  def send(self, to, subject, body, cc=None, attachs=(), _callback=None):
    msg = MIMEText(body)
    msg['To'] = to
    msg['From'] = self.mailfrom
    msg['Subject'] = subject
    self.smtp.sendmail(to, self.mailfrom, msg.as_string())

