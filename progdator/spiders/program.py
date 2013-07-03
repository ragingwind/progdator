# -*- coding: utf-8 -*-

import chardet
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from progdator.items import ProgramItem
from datetime import datetime

class Program(BaseSpider):
  name = "program"
  allowed_domain = ["epg.co.kr"]
  today = datetime.now().strftime("%Y-%m-%d")
  start_urls = ["http://schedule.epg.co.kr/new/tvguide/tvguide.php?ymd=" + today + "&search_top_channel_group=1&old_top_channel_group=1&search_sub_channel_group=200&old_sub_channel_group=200&search_top_category=&search_sub_category=&mychannel=&checkchannel%5B270%5D=CJB+%C3%BB%C1%D6%B9%E6%BC%DB&checkchannel%5B13%5D=EBS&checkchannel%5B269%5D=G1+%B0%AD%BF%F8%B9%CE%B9%E6&checkchannel%5B376%5D=JIBS+%C1%A6%C1%D6%B9%E6%BC%DB&checkchannel%5B271%5D=JTV+%C0%FC%C1%D6%B9%E6%BC%DB&checkchannel%5B266%5D=KBC+%B1%A4%C1%D6%B9%E6%BC%DB&checkchannel%5B9%5D=KBS1&checkchannel%5B7%5D=KBS2&checkchannel%5B264%5D=KNN+%BA%CE%BB%EA%B0%E6%B3%B2%B9%E6%BC%DB&checkchannel%5B11%5D=MBC&checkchannel%5B816%5D=OBS+%B0%E6%C0%CETV&checkchannel%5B6%5D=SBS&checkchannel%5B265%5D=TBC+%B4%EB%B1%B8%B9%E6%BC%DB&checkchannel%5B267%5D=TJB+%B4%EB%C0%FC%B9%E6%BC%DB&checkchannel%5B268%5D=UBC+%BF%EF%BB%EA%B9%E6%BC%DB&checkchannel%5B281%5D=%B0%E6%C0%CE+KBS1&checkchannel%5B574%5D=%B8%F1%C6%F7+KBS1&checkchannel%5B565%5D=%BF%F8%C1%D6+KBS1&checkchannel%5B572%5D=%C3%E6%C1%D6+KBS1"]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//td/a[contains(@onmouseover,"Preview")]/@onmouseover')
    items = []
    for site in sites:
      item = ProgramItem()
      extract_param = site.extract()

      ret_data = self.extract(extract_param)

      if 7 !=  len(ret_data):
        continue

      year = str(datetime.today().year) + '/'

      item['img'] = ret_data[0][1:-1]
      item['title'] = ret_data[1][1:-1]
      item['channel'] = ret_data[2][1:-1]
      time = ret_data[3][1:-1].split('~')
      item['start_time'] = datetime.strptime(year + time[0].replace('<br>',''), '%Y/%m/%d %p %I:%M')
      item['end_time'] = datetime.strptime(year + time[1], '%Y/%m/%d %p %I:%M')
      item['category'] = ret_data[4][1:-1]
      item['cast'] = ret_data[5][1:-1]
      item['dirt'] = ret_data[6][1:-1]
      items.append(item)
    return items

  def extract(self, param):
    item = []
    start_index = param.find('Preview(')
    end_index = param.rfind(')');
    phase_one = param[start_index + 8 : end_index - len(param) ]
    item = phase_one.split(',')
    return item
