import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\Greenish\\Downloads\\chat-6fdfa-54c7ebf2b0b9.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chat-6fdfa.firebaseio.com'
})

ref = db.reference('/')
print(ref.get())
ref.set('chats')
chats_ref = ref.child('chats')
chats_ref.update({"0": {
    'name': 'MedChat',
    'sender_id': '00000',
    'text': 'hi how are you'

}})
i = 1

while(True):
    try:
        lst = ref.child('chats').get()
        print(lst.keys())
    except:
        print("dam")
    time.sleep(1)
