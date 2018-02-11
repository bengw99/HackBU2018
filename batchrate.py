from requestTest import *

def batch_rate(messages):
    for message in messages:
        message.set_safety_rating(checkURL(message.get_url()))
