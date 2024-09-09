from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7458134467:AAHbww6ANjxo2SA-J3-Mwr_35FKihhM1h5c' 

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Bu mening shablon bilan integratsiya qilingan botim.")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
