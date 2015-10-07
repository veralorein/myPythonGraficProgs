# -*- coding: utf-8 -*-
import urllib
url = "https://www.youtube.com/watch?v=LjCzPp-MK48"
webFile = urllib.urlopen(url)
localFile = open(url.split('/')[-1], 'wb')
localFile.write(webFile.read())
webFile.close()
localFile.close()