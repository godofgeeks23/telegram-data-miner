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
