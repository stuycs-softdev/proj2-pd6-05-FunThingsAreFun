from urllib2 import Request, urlopen, URLError


#$.ajax({
#  url: 'http://api.randomuser.me/0.2',
#  dataType: 'json',
#  success: function(data){
#    console.log(data);
#  }
#});

def getStuff():
    request = Request('http://api.randomuser.me/0.2')
    
    try:
	response = urlopen(request)
	results = response.read()
	
        #results=results.lstrip('{"results":')
        #results=results.rstrip("}")
        #print results
        user={"gender":"",
              "name":"",
              "location":"",
              "email":"",
              "password":"",
              "md5_hash":"",
              "sha1_hash":"",
              "phone":"",
              "cell":"",
              "SSN":"",
              "picture":""}
        list=["gender",
              "name",
              "location",
              "email",
              "password",
              "md5_hash",
              "sha1_hash",
              "phone",
              "cell",
              "SSN",
              "picture",
              '"seed"']
        
        #gender = results[results.rfind("gender")+len("gender"):results.rfind("name")]
        #gender=gender[3:-3]
        #print gender
        
        for x in range(0,len(list)-1):
            #print results[results.rfind(list[x])+len(list[x]):results.rfind(list[x+1])][3:-3]
            user[list[x]]=results[results.rfind(list[x])+len(list[x]):results.rfind(list[x+1])][3:-3]
        
        return user

    except URLError, e:
        print 'No response', e
        
def getBio():
    response = urlopen('http://www.twitterbiogenerator.com')
    html = response.read()
    bio = html[1973:html.find('</textarea>')]
    return bio

def getUser():
    x = getStuff()
    x['bio'] = getBio()
    return x
