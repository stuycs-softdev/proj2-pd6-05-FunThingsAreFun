from urllib2 import Request, urlopen, URLError
import json
import random


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
	print 'getstuff'
	response = urlopen(request)
	results = response.read()
	data=json.loads(results)
	data = data['results'][0]['user']

	
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
        
#        for x in range(0,len(list)-1):
            #print results[results.rfind(list[x])+len(list[x]):results.rfind(list[x+1])][3:-3]
#            user[list[x]]=results[results.rfind(list[x])+len(list[x]):results.rfind(list[x+1])][3:-3]
        
	print 'getstuff'
        return data

    except URLError, e:
        print 'No response', e
        
def getBio():
    print 'bio'
    response = urlopen('http://www.twitterbiogenerator.com')
    html = response.read()
    bio = html[1973:html.find('</textarea>')]
    print 'bio'
    return bio

inD = open('indoorhobbies.txt','r').read().split('\r\n')
outD = open('outdoorhobbies.txt','r').read().split('\r\n')
l_inD = len(inD)
l_outD = len(outD)

def getHobbies():
    ret = []
    for x in range(0,3):
	if random.randint(0,1) == 1:
	    temp = {'door':'out','hobby':outD[random.randint(0,l_outD-1)]} 
	else:
	    temp = {'door':'in','hobby':inD[random.randint(0,l_inD-1)]}
	ret.append(temp)
    return ret 

def getOri(sex):
    y = random.randint(0,9)
    if sex == 'male':
	if y == 0:
	    return 'Men'
	else:
	    return 'Women'
    else:
	if y == 0:
	    return 'Women'
	else:
	    return 'Men'

def getUser():
    x = getStuff()
    x['ori'] = getOri(x['gender'])
    x['bio'] = getBio()
    x['hobbies'] = getHobbies()
    return x

