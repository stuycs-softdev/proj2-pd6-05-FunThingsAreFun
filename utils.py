from pymongo import MongoClient
from flask import session
import randomuser
import random
from bson.objectid import ObjectId
import datetime

client = MongoClient()
db = client.ARSS

def record_exists(collection, query, limit=1):
        return collection.find(query, limit=1).count(True) > 0

def user_exists(username):
        return record_exists(db.users, {'username': username})

def validate_user(username, password):
        return record_exists(db.users, {'username': username, 'password': password})

def update_user(username, password):
        db.users.update(
                {'username': username},
                {'password': password},
                upsert=True
        )

def insert_user(username, password):
        db.users.insert(
                {'username': username,
                'password': password}
        )

def login_user(username, password):
        if validate_user(username, password):
                session['username'] = username
                return 'Success!'
        else:
                return 'Incorrect username or password.' 
def logout_user():
        session.pop('username', None)

def register_user(username, password):
        if (user_exists(username)):
                return 'User Already Exists.'
        else:
                insert_user(username, password)
		login_user(username,password)
                return 'Success!'

def change_password(username, password):
        if (len(password) < 4):
                return 'Password too short.'
        else:
                update_user(username, password)
                return 'Success!'

def change_username(username, new_username):
        db.users.update({'username': username}, {'username': new_username})

def logged_in():
        if not user_exists(session.get('username', None)):
                session.pop('username', None)
        return session.get('username', None) != None

def addRandUser(username):
    time = str(datetime.datetime.today()).split('.',1)[0]
    user=randomuser.getUser()
    name = user['name']['first'].capitalize() + " " + user['name']['last'].capitalize()
    location = (user['location']['city'] + ", " + user['location']['state']).title()
    about = user['bio']
    email = user['email']
    cell = user['cell']
    image = user['picture']
    ori = user['ori']
    hobbies = user['hobbies']
    gender = user['gender']
    stuff = {"name":name,"location":location,"about":about,"email":email,"cell":cell,"image":image,"ori":ori,'user':username, 'gender': gender, 'hobbies':hobbies, 'activity':[[0, name + ' has joined AI Dating Site!', time]], 'connections':[]}
    print 'b4 sert'
    db.fakes.insert(stuff)
    del stuff['_id']
    return stuff

def connect(a,b):
    time = str(datetime.datetime.today()).split('.',1)[0]
    a['activity'].append([1, a['name'] + ' has connected with ', b['name'], b['_id'], time])
    a['connections'].append(a['_id'])
    print a['activity']
    db.fakes.update({'_id':a['_id']},{'$set': {'activity': a['activity']}})
    db.fakes.update({'_id':a['_id']},{'$set': {'connections':a['connections']}})
    b['activity'].append([1, b['name'] + ' has connected with ', a['name'], a['_id'], time])
    ba = b['activity']
    b['connections'].append(a['_id'])
    bc = b['connections']
    db.fakes.update({'_id':b['_id']},{'$set': {'activity': b['activity']}})
    db.fakes.update({'_id':b['_id']},{'$set': {'connections':b['connections']}})

def showA():
    return [x['activity'] for x in db.fakes.find()]

def getPro(_id):
    return [x for x in db.fakes.find({'_id':ObjectId(_id)})]

def doStuff():
    ppl = [x for x in db.fakes.find()]
    for p in ppl:
	for x in ppl:
	    if p != x and x['_id'] not in p['connections'] and ((p['ori'] == 'Men' and x['gender'] == 'male') or (p['ori']=='Women' and x['gender'] == 'female')):
		pOI = 0
		xOI = 0
		for ph in p['hobbies']:
		    if ph['door'] == 'out':
			pOI = pOI + 1
		for xh in x['hobbies']:
		    if xh['door'] == 'out':
			xOI = xOI + 1

		chance = pOI - xOI
		chance = 0
		print chance

		if chance == 0:
		    connect(p,x)
		    break
		elif random.randint(0,chance) != 0:
		    connect(p,x)
		    break
