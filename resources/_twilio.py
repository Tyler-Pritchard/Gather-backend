from twilio.rest import Client
import twilio

# Your Test Account SID from twilio.com/console
account_sid = "ACe23db114a4d0ccce327eeeba4e9fad2f"
# Your Auth Token from twilio.com/console
auth_token = "********************"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1520909", from_="+15206399758", body="Hello, Mansoor my name is Python!"
)

print(message.sid)
