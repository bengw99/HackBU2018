def batch_rate(messages):
    for message in messages:
        message.set_safety_rating(0)
