import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(body='IT WORKS!!!!',
                                 from_='whatsapp:+14155238886',
                                 to='whatsapp:'+ os.environ['MY_PHONE_NUMBER'])

print(message.sid)
