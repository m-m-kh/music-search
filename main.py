from telegram.ext import CallbackContext ,Updater, MessageHandler, Filters
from telegram import Update, InlineKeyboardMarkup,InlineKeyboardButton
from tests.test import findmusic

updater = Updater('5567723428:AAGqfiF5XlZaC6r0KcBd_rKZZiLfGvxQOCM')

def search(update:Update, cnotext:CallbackContext):
    result = findmusic(f'آهنگ {update.message.text}')
    keyboard = [[InlineKeyboardButton(text=str(i[1]),url=str(i[0]))] for i in result]
    update.message.reply_text(text=':)',reply_markup=InlineKeyboardMarkup(keyboard))
    # print(keyboard)
    
def breaker(update:Update, cnotext:CallbackContext):
    return

updater.dispatcher.add_handler(MessageHandler(Filters.command,breaker))
updater.dispatcher.add_handler(MessageHandler(Filters.text,search,run_async=True))



# updater.idle()
updater.start_polling()