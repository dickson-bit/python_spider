from urllib2 import Request, urlopen, URLError, HTTPError  
  
  
old_url = 'http://www.baidu.com'
req = Request(old_url)  
response = urlopen(req)
response = urlopen(old_url)

print 'Old url :' + old_url  
print 'Real url :' + response.geturl()
print dir(response)

print response.getcode()

print response.headers
