# Scrapy settings for craigslist project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import yaml

with open("config.yml", 'r') as f:
	config = yaml.load(f)

BOT_NAME = 'craigslist'

SPIDER_MODULES = ['craigslist.spiders']
NEWSPIDER_MODULE = 'craigslist.spiders'

ITEM_PIPELINES = [
    'craigslist.pipelines.CraigslistPipeline',
]

LOG_LEVEL = 'INFO'
if config['log']['tofile']:
	LOG_FILE = config['log']['logfile']

# SPIDER SETTINGS
SEARCH_URLS = config['searches']

# MAIL SETTINGS
mail = config['mail']
MAIL_FROM = mail['from']
MAIL_TO = mail['to']
MAIL_HOST = mail['host']
MAIL_PORT = mail['port']
MAIL_USER = mail['user']
MAIL_PASS = mail['pass']
MAIL_TLS = mail['tls']
MAIL_SSL = mail['ssl']

# OUTPUT SETTINGS
TMP_FILE = config['output']['tmp']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist (+http://www.yourdomain.com)'
