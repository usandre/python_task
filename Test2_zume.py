# -*- coding: utf-8 -*-

import sys
import os
import urllib2
import json

# Complete the function below.

def getMovieTitles(substr):
    data = json.load(urllib2.urlopen('https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr))

    pages = data['total_pages']
    arr = []

    for page in range(1,pages):
        data = json.load(urllib2.urlopen('https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr+ '&page=' + str(page)))
        for i in data['data']:
            arr.append(i['Title'])

    arr.sort()
    return arr


print(getMovieTitles('Spi'))