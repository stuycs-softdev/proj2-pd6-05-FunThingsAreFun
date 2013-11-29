#!/usr/bin/env python

import urllib2

#get bio
def getbio():
    response = urllib2.urlopen('http://www.twitterbiogenerator.com')
    html = response.read()
    print html
    bio = html[1973:html.find('</textarea>')]
    print bio
    return bio

getbio()
