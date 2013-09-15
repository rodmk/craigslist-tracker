from craigslist.items import CraigslistItem
from scrapy.conf import settings
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.utils.response import get_base_url
from urlparse import urljoin

class CraigslistSpider(BaseSpider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = settings["SEARCH_URLS"]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    base_url = get_base_url(response)
    titles = hxs.select("//span[@class='pl']")
    for titles in titles:
      item = CraigslistItem()
      item["title"] = titles.select("a/text()").extract()[0]
      relative_url = titles.select("a/@href").extract()[0]
      item["link"] = urljoin(base_url, relative_url)
      yield item
