from telegram.ext import Updater, CommandHandler
import requests


def get_price():
    contents = requests.get(
        'https://api.coinbase.com/v2/prices/spot?currency=USD')
    price = contents.json()['data']['amount']
    return price


def bop(bot, update):
    price = get_price()
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id, text="at this time BTC price is :" + price)


def main():
    updater = Updater('your telegram bot token')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
