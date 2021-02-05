import asyncio
import logging
from time import sleep

from telegram import Update, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from datetime import datetime

from Gadgets.console_colors import bcolors

updater = Updater(token='1618156264:AAG4JRzGQD3O-gEjD3yFzS5OssJQiJML5j4', use_context=True) #Replace TOKEN with your token string
telegarm_bot = updater.dispatcher

print("Start")

## Conversation To get profile users

# Enable logging
logging.basicConfig(
    format=f'''{bcolors.Yellow}
    %(asctime)s - %(name)s - %(levelname)s - %(message)s {bcolors.Normal}''',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
BIO, FINISH = range(2)

def cancel(update: Update, context: CallbackContext): # -> int: (return as int)
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', # reply_markup=ReplyKeyboardRemove()
    )

def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'You seem a bit paranoid! ' 'At last, tell me something about yourself.'
    )

    return BIO


def bio(update: Update, context: CallbackContext) -> int:
    last_input = update.message.text
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, last_input)
    update.message.reply_text(f'users: {last_input}.')

    return ConversationHandler.END

# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', skip_location)],
    states={
        BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
telegarm_bot.add_handler(conv_handler)

# ------------------------------------------

# Any Text (unless Fortnite)
def reply(update, context):
    user_input = update.message.text
    if "ortnit" in user_input or "פורטנ" in user_input:
        update.message.reply_text(f"{user_input}? \nרציני אחי? \nאתה מגעיל אותי.") #AKA print
    else:
        update.message.reply_text("You have wrote me \n" + user_input) #AKA print
telegarm_bot.add_handler(MessageHandler(Filters.text, reply))

# Any unknown command "MessageHandler(Filters.command, unknown)"
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
unknown_handler = MessageHandler(Filters.command, unknown)
telegarm_bot.add_handler(unknown_handler)

updater.start_polling()
