from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

updater = Updater(token='1618156264:AAG4JRzGQD3O-gEjD3yFzS5OssJQiJML5j4', use_context=True) #Replace TOKEN with your token string
telegarm_bot = updater.dispatcher

print("Start")

# secret hello command on bot (secret because not in @BotFather command list)
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
hello_handler = CommandHandler('hello', hello) # CommandHandler
telegarm_bot.add_handler(hello_handler)

# date command on bot
def date(update, context):
    today = datetime.today().date()
    today_name = datetime.now().strftime("%A")
    def date_translator(ttoday_name):
        if ttoday_name == "Sunday": ttoday_name = "ראשון"
        if ttoday_name == "Monday": ttoday_name = "שני"
        if ttoday_name == "Tuesday": ttoday_name = "שלישי"
        if ttoday_name == "Wednesday": ttoday_name = "רביעי"
        if ttoday_name == "Thursday": ttoday_name = "חמישי"
        if ttoday_name == "Friday": ttoday_name = "שישי"
        if ttoday_name == "Saturday": ttoday_name = "שבת"
        return ttoday_name
    today_name = date_translator(today_name)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{today}\n {today_name}")
date_handler = CommandHandler('date', date) # CommandHandler
telegarm_bot.add_handler(date_handler)

# time command on bot
def time(update, context):
    my_time = datetime.now().strftime("%H:%M:%S") # 16:31:59
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{my_time}")
time_handler = CommandHandler('time', time) # CommandHandler
telegarm_bot.add_handler(time_handler)

# Any unknown command "MessageHandler(Filters.command, unknown)"
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
unknown_handler = MessageHandler(Filters.command, unknown)
telegarm_bot.add_handler(unknown_handler)

# Any Text (unless Fortnite)
def reply(update, context):
    user_input = update.message.text
    if "ortnit" in user_input or "פורטנ" in user_input:
        update.message.reply_text(f"{user_input}? \nרציני אחי? \nאתה מגעיל אותי.") #AKA print
    else:
        update.message.reply_text("You have wrote me \n" + user_input) #AKA print
telegarm_bot.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
