from telegram.ext import CallbackContext ,Updater, MessageHandler, Filters
from telegram import Update,ParseMode
from tests.test import findmusic, requests
import os
updater = Updater('5567723428:AAHfA4UJdJdzG1tBqmNe3xXXOZYTxADHI8I')

def search(update:Update, context:CallbackContext):
    msgid = update.message.reply_text('searching on google...').message_id
    result = findmusic(f'آهنگ {update.message.text}')
    context.bot.delete_message(chat_id=update.message.chat_id,message_id=msgid)
    for i in result:
        update.message.reply_text(f"<a href='{i[0]}'>Download</a>\n{i[1]}",parse_mode=ParseMode.HTML)
    
    
def breaker(update:Update, cnotext:CallbackContext):
    return

updater.dispatcher.add_handler(MessageHandler(Filters.command,breaker))
updater.dispatcher.add_handler(MessageHandler(Filters.text,search,run_async=True))


PORT = int(os.environ.get('PORT', 8443))
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path='5463247683:AAHddBkYmx9hvjKoLU5KvKOPRI21AqTGFVY', webhook_url='https://music-c11a.onrender.com/' + '5463247683:AAHddBkYmx9hvjKoLU5KvKOPRI21AqTGFVY')
updater.idle()
