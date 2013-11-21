from urllib2 import Request, urlopen, URLError

#$.ajax({
#  url: 'http://api.randomuser.me/0.2',
#  dataType: 'json',
#  success: function(data){
#    console.log(data);
#  }
#});

request = Request('http://api.randomuser.me/0.2')

try:
	response = urlopen(request)
	read = response.read()
	print read
        results=read["results"][0]
        print results

except URLError, e:
    print 'No response', e

