1. On the top left corner click “Create”

![pic 1](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/1.png?raw=true)

2. A new window will appear. Click “Import from GitHub”

![pic 2](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/2.png?raw=true)

3. Paste the repository link and click the blue button “Import from GitHub”
```
https://github.com/Makrine/TelegramAutoResponder
```

![pic 3](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/3.png?raw=true)

4. Select “src/main.py” here and click “Done”

![pic 4](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/4.png?raw=true)

5. Now set your secrets (API keys) by pressing Secrets on the left side here.

![pic 5](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/5.png?raw=true)

6. You can either enter all Keys manually or just click “Open raw editor” and paste the following JSON there. Make sure to insert your own API keys though.
```
{
  "OPENAI_API_KEY": "openai_api_kei",
  "TELEGRAM_API_ID": "telegram_api_id",
  "TELEGRAM_API_HASH": "telegram_api_hash",
  "PHONE": "phone_number1",
  "PHONE2": "phone_number2"
}
```
![pic 6](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/6.png?raw=true)

7. It should look like this

![pic 7](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/7.png?raw=true)

8. Navigate to main.py and uncomment the second and the 12th lines. It should look like this

![pic 8](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/8.png?raw=true)

9. Now click “Run” on top and wait for it to install packages. After installation is done, it will ask you the following where  you have to enter your Telegram phone number (also include the country code without “+” sign)

You will receive a code on your Telegram and enter it on the second line. After that you will see the success message.

![pic 9](https://github.com/Makrine/TelegramAutoResponder/blob/master/HowToReplit/9.png?raw=true)

10. And that’s it. After this you can even shut down your computer and it will work. It might stop working for some unexplained reason though. So if it doesn’t work anymore just check if your replit is running.
