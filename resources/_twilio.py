from twilio.rest import Client
import twilio

# Your Account SID from twilio.com/console
account_sid = "AC7e7637f7467d96072babdbafc41d8509"
# Your Auth Token from twilio.com/console
auth_token = "d4a16cbf919c613e198c392b1ee8f609"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15209095372",
    from_="+15206399758",
    body="Hello, Mansoor my name is Python!")

print(message.sid)
