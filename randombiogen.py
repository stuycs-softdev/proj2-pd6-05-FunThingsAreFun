import urllib2
response = urllib2.urlopen('http://www.twitterbiogenerator.com')
html = response.read()
print html
bio = html[1973:2072]
print bio
