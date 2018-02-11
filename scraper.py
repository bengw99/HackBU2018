from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import google.oauth2.credentials
import google_auth_oauthlib.flow
import email

from auth import *

class Sender():
    url = ""
    count = 0
    safety_rating = None

    def __init__(self, url):
        self.url = url
        self.count += 1

    def get_url(self):
        return self.url

    def get_count(self):
        return self.count

    def get_safety_rating(self):
        return self.safety_rating

    def increment_count(self):
        self.count += 1
        return

    def set_safety_rating(self, safety_rating):
        self.safety_rating = safety_rating
        return

def make_sender(url):
    sender = Sender(url)
    return sender

def scrape(code):
# Making variables
    list_of_senders = []
    auther = Auther()
    auther.get_flow().fetch_token(code = code)
    session = auther.get_flow().authorized_session()
    messages = session.get('https://www.googleapis.com/gmail/v1/users/me/messages/?q="in:inbox"').json().get('messages')

# Finding messages
    for message in messages:
        message_id = message.get('id')
        http_request = 'https://www.googleapis.com/gmail/v1/users/me/messages/' + message_id
        headers = session.get(http_request).json().get('payload').get('headers')
        sender_url = None

# Getting 'From' values
        for header in headers:
            if header.get('name') == 'From':
                sender = header.get('value') 
                if ">" in sender:
                    sender_url = sender[sender.find('@')+1:sender.find('>')]
                else:
                    sender_url = sender[sender.find('@')+1:len(sender)]
                if ">" in sender_url or "<" in sender_url or "@" in sender_url:
                    sender_url = None
        if sender_url == None:
            continue

# Discovering who sent you mail
        found = False
        for current_sender in list_of_senders:
            if(current_sender.get_url() == sender_url):
                current_sender.increment_count()
                found = True
        if found == False:
            list_of_senders.append(make_sender(sender_url))
        print("Sender Url: %s \n\t Sender: %s" % (sender_url, sender))
# Checking Sender class
    for csender in list_of_senders:
        print("URL: %s \n\t NUMBER %d" % (csender.get_url(), csender.get_count()))
    return list_of_senders 
