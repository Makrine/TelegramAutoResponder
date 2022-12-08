# TelegramAutoResponder
Auto reply to specific people on Telegram using OpenAI

# How-To

You need to create API keys for [OpenAI](https://beta.openai.com/account/api-keys) and [Telegram](https://my.telegram.org/).

* install requirements using

```
pip install -r requirements.txt
```

* create ```.env``` file and write your API keys there.

template for ```.env```:

```
OPENAI_API_KEY = "openai_api"
TELEGRAM_API_ID = telegram_api_id
TELEGRAM_API_HASH = "telegram_api_hash"

PHONE = "phone_number1"
# PHONE2 = "phone_number2"

```

* run ```main.py```


# How to run the code on server using Replit

If you just run ```main.py``` on your computer, it will work just fine but after you close it, it will stop working. However, you can use Replit to make the code run on server.

You can follow [this tutorial](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/HowToReplit.md).
