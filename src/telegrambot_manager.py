import time
from decouple import config
from telethon import TelegramClient, events
import asyncio
from openai_manager import *

# set up api key stuff
api_id = config('TELEGRAM_API_ID')
api_hash = config('TELEGRAM_API_HASH')

# start telegram session
client = TelegramClient('session', api_id, api_hash)

# phone numbers of people you want to autorespond
from_phone_number = [config('PHONE')] # for more numbers: [config('PHONE'), config('PHONE2')]


@client.on(events.NewMessage)
async def handle_new_message(event):

    try:
        from_user = await event.client.get_entity(event.from_id)
        print(time.asctime() + " - A new message from: " + from_user.phone)
        print("Message: " + event.message.message)
        if from_user.phone in from_phone_number: 
            async with client.action(from_user.phone, 'typing'):
                message = event.message.message
                reply = get_ai_reply(message)
                print(time.asctime() + " - AI reply: " + reply)
                await asyncio.sleep(2)
                await client.send_message(from_user.phone, reply)
    except Exception as e:
        print(e)
