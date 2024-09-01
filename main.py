import cfg
#import time
from telegram import Update, User
from telegram.ext import Updater, MessageHandler, CallbackContext, ContextTypes, Filters


def new_member(update, context):
    for member in update.message.new_chat_members:
        update.message.reply_text('Добро пожаловать, @' + member.username + cfg.WELCOME_MESSAGE)
        #member = User.username
        #if member.username is not None:
        #    update.message.reply_text('Добро пожаловать, @' + member.username + cfg.welcome_message)
        #else:
        #    update.message.reply_text('Добро пожаловать, ' + member.first_name + cfg.welcome_message)


def main() -> None:

    #time.sleep(3)
    updater = Updater(cfg.API_TOKEN)
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

