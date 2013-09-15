# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os.path
# TODO: Switch to using the scrapy mail sender
from craigslist.mail import MailSender

class CraigslistPipeline(object):
  def __init__(self, settings):
    self.filepath = settings["TMP_FILE"]
    self.mailto = settings["MAIL_TO"]
    self.firstrun = not os.path.exists(self.filepath)
    self.file = open(self.filepath, 'a+')
    self.seenurls = set()
    for line in self.file:
      self.seenurls.add(line.rstrip())

    # set up e-mail
    self.mailer = MailSender.from_settings(settings)

  @classmethod
  def from_crawler(cls, crawler):
    return cls(crawler.settings)

  def process_item(self, item, spider):
    if self.firstrun or (not item['link'] in self.seenurls):
      self.file.write('%s\n' % item['link'])
      if not self.firstrun:
        self.send_mail(item)
    return item

  def send_mail(self, item):
    self.mailer.send(
      to=self.mailto,
      subject="[Craigslist] %s" % item['title'],
      body=item['link'],
    )
