# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ProgramItem(Item):
	title = Field()
	img = Field()
	channel = Field()
	start_time = Field()
	end_time = Field()
	category = Field()
	cast = Field()
	dirt = Field()
