import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from random import random
import config

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\Greenish\\Downloads\\chat-6fdfa-54c7ebf2b0b9.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chat-6fdfa.firebaseio.com'
})
config.x = 0
ref = db.reference('/')
ref.set('chats')
chats_ref = ref.child('chats')

def ignore_first_call(fn):
    called = False

    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            return fn(*args, **kwargs)
        else:
            called = True
            return None

    db.reference('chats').update({"0": {
        'name': 'MedChat',
        'sender_id': '00000',
        'text': 'hi how are you'

    }})
    return wrapper

def sendResponse():
    text1 = input("resposne?: ")
    config.x+= 1
    chats_ref.update({"{}".format(config.x): {
        'name': 'MedChat',
        'sender_id': '00000',
        'text': text1

    }})

@ignore_first_call
def listener(event):
    if (event.event_type == 'put'):

        print(event.event_type)  # can be 'put' or 'patch'
        print(event.path)  # relative to the reference, it seems
        print(event.data)  # new data at /reference/event.path. None if deleted
        # print(event.data['name'])
        # print(event.data['sender_id'])
        # print(event.data['text'])
        sendResponse()

    """node = str(event.path).split('/')[-2] #you can slice the path according to your requirement
    property = str(event.path).split('/')[-1]
    value = event.data"""





db.reference('chats').listen(listener)