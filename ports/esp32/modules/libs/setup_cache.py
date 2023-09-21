import json

from libs.config_dataclasses import StoredSetupMessage
from messages.setup_message_upb2 import SetupMessage

setup_data: StoredSetupMessage
with open('store/cache/setup_message_data.json','r',encoding='utf8') as file:
    setup_message_dict = json.loads(file.read())
    setup_data = StoredSetupMessage(**setup_message_dict)

def save_setup_message():
    '''Save the current setup message metadata in cache'''
    global setup_data
    with open('store/cache/setup_message_data.json','w',encoding='utf8') as file:
        print(setup_data.toJSON())
        file.write(setup_data.toJSON())
