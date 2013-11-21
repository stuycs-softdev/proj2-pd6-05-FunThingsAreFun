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
	results = response.read()
	#print results
        results=results.lstrip('{"results":')
        results=results.rstrip("}")
        print results
        
        print results[results.rfind("gender"):results.rfind("gender")+len("gender")]
        user={}
        
except URLError, e:
    print 'No response', e

