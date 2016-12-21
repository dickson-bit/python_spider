import urllib2
try:
    response = urllib2.urlopen('http://restrict.web.com')
except urllib2.HTTPError, e:
    print e.code
