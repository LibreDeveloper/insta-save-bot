# Insta save telegram bot
a simple telegram bot to download media from instagram.
## Requirements
1. Getting instagram account session cookies
  - Intsgram has limited API, it needs a csrf token to response to reqeusts. best way to get the cookies is create an account on instagram then capture cookie with any traffic capture program(Telerik Fiddler will do the trick for you!). and after you capture cookie put it on 'Cookies.py' related variable. NOTE: DON'T LOG OUT FROM CREATED ACCOUNT! IT WILL DISPOSE COOKIE!
2. Create a telegram bot
  - Send a message to [BotFather](https://t.me/BotFather) then create a bot and copy your bot token then paste it in 'app.py' related variable.
3. Dont forget to run `pip install requirements.txt`
3. Your ready to go!
  - there is 2 methods to run the bot
    1. Using polling method, best for VPS or local machine computer
    2. Using webhook method, best for pyton hosts like Heroku
## Where can i run the bot?
1. Heroku
  - Best for both polling and webhook method BUT, they are gonna remove there free tier in future!
2. Pythonanywhere
  - you can use polling method in this website for free!

## [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) used in this project to communicate with telegram bot api endpoints.
