# Scrapy settings for progdator project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

import sys

# DEFAULTS
BOT_NAME = 'progdator'
SPIDER_MODULES = ['progdator.spiders']
NEWSPIDER_MODULE = 'progdator.spiders'
ITEM_PIPELINES = ['progdator.pipelines.MongoDB']

# MONGGODB
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "progdator"
MONGODB_COLLECTION_PROGRAMS = "programs"
MONGODB = any('mongodb=true' == arg for arg in sys.argv)

# LOG
LOG_LEVEL = 'WARNING'
