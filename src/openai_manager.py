import openai
from decouple import config

def format_reply(reply):
    # if there is a new line in the reply, remove everything before the new line. Because
    # the new line means completion of the message (if there is only one new line)
    # this will fail if the reply message is actually 2 paragraph long
    first_inedx = -1
    new_line_counter = 0

    for i, c in enumerate(reply):
        if '\n' == c and first_inedx == -1:
            first_inedx = i # remember the index
            new_line_counter += 1  # increment new line counter
    
    if new_line_counter == 1:
        reply = reply[first_inedx:]
    
    return reply


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

    reply = response['choices'][0]['text']

    reply = format_reply(reply)
            
    return reply

# set up api key stuff
openai.api_key = config('OPENAI_API_KEY')