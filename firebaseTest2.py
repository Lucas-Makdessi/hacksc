import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from map_reader import getSetIntsersection
import config

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\Greenish\\Downloads\\chat-6fdfa-54c7ebf2b0b9.json')

#cred = credentials.Certificate("/Users/lucasmakdessi/Downloads/chat-6fdfa-54c7ebf2b0b9.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chat-6fdfa.firebaseio.com'
})
config.x = 0
ref = db.reference('/')
ref.set('chats')
chats_ref = ref.child('chats')

# a method to ignore the first query pulled by the listener because this represents
# the own program's first udpate
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
        'text': 'Hi this is Dr. MedBot, how may I help you?'

    }})
    return wrapper

# a method called by the python listener to respond with a text output given a question
def sendResponse(question):
    text = ""
    if question.lower() == "thanks" or question.lower() == "thank you":
        text = "Anything else I can help you with?"
    # assuming that user correctly enters 1 or 2 to select the option and not some junk
    elif question == "1" or question == "2":
        text = config.setthing[int(question)-1][1]
    else:
        set1 = getSetIntsersection(question)

        if type(set1) is str:
            text = set1
        else:
            config.setthing = set1
            text = "I found two similiar questions, which would best fit your question?\n1) {}\n2) {}".format(set1[0][0],set1[1][0])
            #text = ', '.join(str(e[1]) for e in set1)

    config.x+= 1
    chats_ref.update({"{}".format(config.x): {
        'name': 'MedChat',
        'sender_id': '00000',
        'text':text

    }})

# a listener to listen for updates to the database
@ignore_first_call
def listener(event):
    #only want put events because the user does put events and the program does patch events
    #and we only want to respond to user input
    if (event.event_type == 'put'):

        print(event.event_type)  # can be 'put' or 'patch'
        print(event.path)  # relative to the reference, it seems
        print(event.data)  # new data at /reference/event.path. None if deleted
        # print(event.data['name'])
        # print(event.data['sender_id'])
        # print(event.data['text'])
        sendResponse(event.data['text'])

    """node = str(event.path).split('/')[-2] #you can slice the path according to your requirement
    property = str(event.path).split('/')[-1]
    value = event.data"""





db.reference('chats').listen(listener)