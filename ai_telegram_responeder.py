import openai
from decouple import config
from telethon import TelegramClient, events
import time
import random


def get_ai_reply(msg):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=msg,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return(response['choices'][0]['text'])


# set up api key stuff
openai.api_key = config('OPENAI_API_KEY')
api_id = config('TELEGRAM_API_ID')
api_hash = config('TELEGRAM_API_HASH')

# phone number of the person you want to autorespond
from_phone = config('PHONE')


# start telegram session
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage)
async def handle_new_message(event):

    from_user = await event.client.get_entity(event.from_id)
    print(from_user.phone)
    if from_user.phone == from_phone:
        message = event.message.message
        reply = get_ai_reply(message)
        await client.send_message(from_phone, reply)


print(time.asctime(), '-', 'Auto-replying...')
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Stopped!')




