import configparser
import json
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)
client.start()
print("Client Created")
# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))

# getting channel member info
user_input_channel = input("enter entity(telegram URL or entity id):")

if user_input_channel.isdigit():
    entity = PeerChannel(int(user_input_channel))
else:
    entity = user_input_channel

my_channel = client.get_entity(entity)
offset = 0
limit = 100
all_participants = []

while True:
    participants = client(GetParticipantsRequest(
        my_channel, ChannelParticipantsSearch(''), offset, limit,
        hash=0
    ))
    if not participants.users:
        break
    all_participants.extend(participants.users)
    offset += len(participants.users)

all_user_details = []
for participant in all_participants:
    all_user_details.append(
        {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
         "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})

with open('user_data.json', 'w') as outfile:
    json.dump(all_user_details, outfile)