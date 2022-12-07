from telegram.ext import CallbackContext ,Updater, MessageHandler, Filters
from telegram import Update, InlineKeyboardMarkup,InlineKeyboardButton
from tests.test import findmusic
import os
updater = Updater('5567723428:AAHfA4UJdJdzG1tBqmNe3xXXOZYTxADHI8I')

def search(update:Update, cnotext:CallbackContext):
    result = findmusic(f'آهنگ {update.message.text}')
    keyboard = [[InlineKeyboardButton(text=str(i[1]),url=str(i[0]))] for i in result]
    update.message.reply_text(text=':)',reply_markup=InlineKeyboardMarkup(keyboard))
    # print(keyboard)
    
def breaker(update:Update, cnotext:CallbackContext):
    return

updater.dispatcher.add_handler(MessageHandler(Filters.command,breaker))
updater.dispatcher.add_handler(MessageHandler(Filters.text,search,run_async=True))


PORT = int(os.environ.get('PORT', 8443))
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path='5463247683:AAHddBkYmx9hvjKoLU5KvKOPRI21AqTGFVY', webhook_url='https://music-c11a.onrender.com/' + '5463247683:AAHddBkYmx9hvjKoLU5KvKOPRI21AqTGFVY')
updater.idle()
