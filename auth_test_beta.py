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
# # getting channel members info

# user_input_channel = input("enter entity(telegram URL or entity id):")
# if user_input_channel.isdigit():
#     entity = PeerChannel(int(user_input_channel))
# else:
#     entity = user_input_channel
# my_channel = client.get_entity(entity)
# offset = 0
# limit = 100
# all_participants = []
# while True:
#     participants = client(GetParticipantsRequest(
#         my_channel, ChannelParticipantsSearch(''), offset, limit,
#         hash=0
#     ))
#     if not participants.users:
#         break
#     all_participants.extend(participants.users)
#     offset += len(participants.users)
# all_user_details = []
# for participant in all_participants:
#     all_user_details.append(
#         {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
#          "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})
# with open('user_data.json', 'w') as outfile:
#     json.dump(all_user_details, outfile)
# # print(all_user_details)
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# # Getting channel messages

# user_input_channel = input("enter entity(telegram URL or entity id):")
# if user_input_channel.isdigit():
#     entity = PeerChannel(int(user_input_channel))
# else:
#     entity = user_input_channel
# my_channel = client.get_entity(entity)
# offset_id = 0
# limit = 100
# all_messages = []
# total_messages = 0
# total_count_limit = 0

# while True:
#     print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
#     history = client(GetHistoryRequest(
#         peer=my_channel,
#         offset_id=offset_id,
#         offset_date=None,
#         add_offset=0,
#         limit=limit,
#         max_id=0,
#         min_id=0,
#         hash=0
#     ))
#     if not history.messages:
#         break
#     messages = history.messages
#     for message in messages:
#         all_messages.append(message.to_dict())
#     offset_id = messages[len(messages) - 1].id
#     total_messages = len(all_messages)
#     if total_count_limit != 0 and total_messages >= total_count_limit:
#         break
# # with open('message_data.json', 'w') as outfile:
#     # json.dump(all_messages, outfile)
# print(all_messages)
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# Searching channels


def search_channels():
    results = []
    search_keywords = ["drugs", "marijuana", "cocaine", "tylenol", "Oxycodone", "Ritalin", "Adderall ", "Oxycotine", "Diazepam Valium", "Xanax", "Dilaudid", "Hydrocodone ", "Percocet ", "MDMA ", "Tramadol", "Suboxone", "Rohypnol", "Tilidin", "Concerta", "Morphine", "Opana", "Oxynorm", "Mandrax", "Quaalude", "Codeine", "LortabWatson", "Dilaudid ", "Fentanyl", "Stilnox ", "viagra", "Subutex", "lyrica", "vicodine5", "seconal", "Dexedrine", "Morphine", "Xanax", "Diazepam", "Methadone", "Oxycodone", "Heroin", "Percocet", "Subutex", "Hydrocodone", "Methadone", "Lyrica", "Adderall", "Diazepam", "Roxicodone", "Rohypnol", "Vicodin", "Benzodiazepines", "Clozapine", "Colchicine", "smuggle", "smuggling", "drugs smuggling", "drugs trafficking", "escort services", "escorts", "call girl", "escorts india", "darkweb", "dark web", "onion", "onion sites", "dark web links", "malware", "ransomware", "carding", "criminal", "deep web", "deepweb", "onion links", "malware mods", "child porn", "porn onion", "dark web porn", "child porn onion", "guns", "buy guns", "dark web guns", "india drug", "indian drugs", "ganja", "marijuana", "buy marijuana", "marijuana market", "marijuana east", "afeem", "afeem india", "afeem delhi", "charas", "charas india", "hashish", "hashish india", "hashish buy"
                       ]
    for search in search_keywords:
        result = client(functions.contacts.SearchRequest(
            q=search,
            limit=1000
        ))
        # print(result.stringify())
        # print(result)
        for section in result.chats:
            print(f"t.me/{section.username}")
        for section in result.users:
            print(f"t.me/{section.username}")

            # print()
        # print(len(result.my_results) + len(result.results) + len(result.chats) + len(result.users), f"Results found for query: {search}")
        # print()
        # print()
        results.append(result)
    total_results_count = 0
    for result in results:
        total_results_count += len(result.my_results) + \
            len(result.results) + len(result.chats) + len(result.users)

    print(f"Total: {total_results_count}")


# ---------------------------------------------------------------------------------------------------------
search_channels()
