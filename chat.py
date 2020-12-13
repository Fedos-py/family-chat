def send_message(sender, recipient, message):
    print(f'User: {sender} texted for {recipient}:')
    print(message)

send_message('Fedos', 'Feodor', "Hi! It's my first message :)")
send_message('Feodor', 'Fedos', "Hi! How are you?")