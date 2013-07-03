# PROGDATOR
EGP Program Predator, It's simple EPG crawler for epg.co.kr. This crawler going to get EPG program data from epg.co.kr. Please check out simple use case below.

## OPTIONS

* `-a mongodb=[true|false]`

  You can select that using mongodb. If you're not ready to use mongodb? You should be use option that `-a mongodb=false`.

## HOW TO RUN

    scrapy crawl program --logfile=progdator.log --loglevel=DEBUG -a mongodb=false

  or If you want to dump data to file as json

    scrapy crawl program -o programs.json -t json --logfile=progdator.log --loglevel=DEBUG -a mongodb=false

  or If you want to use scrapyd

    curl http://localhost:6800/schedule.json -d project=progdator -d spider=program
