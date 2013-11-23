from pymongo import MongoClient
from flask import session

client = MongoClient()
db = client.ARSS

def record_exists(collection, query, limit=1):
        return collection.find(query, limit=1).count(True) > 0

def user_exists(username):
        return record_exists(db.users, {'username': username})

# used to validate login
def validate_user(username, password):
        return record_exists(db.users, {'username': username, 'password': password})

def upsert_user(username, password):
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

# used for register
# user must type password 2 times to make account
def register_user(username, password, confirm_password):
        if (user_exists(username)):
                return 'User Already Exists.'
        elif (len(password) < 4):
                return 'Password too short.'
        elif (password != confirm_password):
                return 'Password does not match confirmation.'
        else:
                insert_user(username, password)
                return 'Success!'

# used to change password
# type in new password two times
def change_password(username, password, confirm_password):
        if (len(password) < 4):
                return 'Password too short.'
        elif (password != confirm_password):
                return 'Password does not match confirmation.'
        else:
                upsert_user(username, password)
                return 'Success!'

# used to change username
def change_username(username, new_username):
        db.users.update({'username': username}, {'username': new_username})

def logged_in():
        if not user_exists(session.get('username', None)):
                session.pop('username', None)
        return session.get('username', None) != None
