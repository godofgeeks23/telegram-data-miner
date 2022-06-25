import configparser
import json
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)
import telethon.sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
from telethon.sync import TelegramClient
from telethon import functions, types

# ---------------------------------------------------------------------------------------------------------
# Reading Configs

config = configparser.ConfigParser()
config.read("config.ini")
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# Setting configuration values

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
phone = config['Telegram']['phone']
username = config['Telegram']['username']
passwd = config['Telegram']['password']
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
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
        client.sign_in(password=passwd)
# ---------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------
# Get a channel's messages

def get_channel_msgs(channel_link):

    if channel_link.isdigit():
        entity = PeerChannel(int(channel_link))
    else:
        entity = channel_link
    my_channel = client.get_entity(entity)
    for message in client.iter_messages(my_channel):
        # print(message.id, message.text)
        print(message)
        print()
# ---------------------------------------------------------------------------------------------------------

links = []
with open("txts/ch_search_list.txt") as file_in:
    # file.read().splitlines()
    links = file_in.read().splitlines()

i = 1
for link in links:
    print("Reading channel: " + "https://" + link)
    get_channel_msgs("https://" + link)
    i = i-1
    if(i<0): break


# get_channel_msgs("https://t.me/importantlink_shiva")