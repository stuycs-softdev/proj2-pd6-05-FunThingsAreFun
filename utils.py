from pymongo import MongoClient
from flask import session
import randomuser
import random

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
    user=randomuser.getUser()
    name = user['name']['first'].capitalize() + " " + user['name']['last'].capitalize()
    location = (user['location']['city'] + ", " + user['location']['state']).title()
    about = user['bio']
    email = user['email']
    cell = user['cell']
    image = user['picture']
    ori = user['ori']
    hobbies = user['hobbies']
    stuff = {"name":name,"location":location,"about":about,"email":email,"cell":cell,"image":image,"ori":ori,'user':username, 'hobbies':hobbies, 'activity':[[0, name + ' has joined AI Dating Site!']], 'connections':[]}
    print 'b4 sert'
    db.fakes.insert(stuff)
    del stuff['_id']
    return stuff

def connect(a,b):
    db.update({'_id':a['_id']},{'activity': a['activity'].append([1, a['name'] + ' has connected with ', b['name'], b['_id']]), 'connections':b['connections'].append(b['_id'])})
    db.update({'_id':b['_id']},{'activity': b['activity'].apeend([1, b['name'] + ' has connected with ', a['name'], a['_id']]), 'connections':a['connections'].append(a['_id'])})

def doStuff():
    ppl = [x for x in db.fakes.find()]
    for p in ppl:
	for x in ppl:
	    if p != x and x['_id'] not in p['connections']:
		chance = 4
		for ph in p:
		    for xh in x:
			if ph['door'] == xh['door']:
			    chance = chance - 1
		if chance == 4:
		    break
		elif chance == 0:
		    connect(p,x)
		elif random.randint(0,chance) != 0:
		    connect(p,x)
