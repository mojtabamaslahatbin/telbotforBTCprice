from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import requests

def get_price():
    contents = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
    body = contents.json()
    data = body.get('data', {})
    price = data.get('amount', {})
    if not price:
        raise Exception("Price data was empty")
    return price

@run_async
def btc(update, context):
    price = get_price()
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text= f"BTC price is : {price}")

def main():
    updater = Updater('TELEGRAM BOT TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('btc', btc))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()



