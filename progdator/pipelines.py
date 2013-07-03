# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.conf import settings

class MongoDB(object):
  def __init__(self):
    if settings['MONGODB']:
      connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
      db = connection[settings['MONGODB_DB']]
      self.collection = db[settings['MONGODB_COLLECTION_PROGRAMS']]

  def process_item(self, item, spider):
    valid = True
    for data in item:
      if not data:
        valid = False
        raise DropItem('Missing program data of %s' % item)

    if valid:
      print '\n%s Program data has been processed\n%s' % (item['channel'], item)
      if self.collection:
        self.collection.insert(dict(item))

    return item
