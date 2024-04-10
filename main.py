import telebot

bot = telebot.TeleBot('6824276007:AAFXqFkU8Re5n7fWxPzh4bWH9v5sjOH-xZw')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name} how can I help you?')

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = """
    The list of available commands:
    /start - to start conversation with bot
    /help - to get a list of available commands
    """
    bot.send_message(message.chat.id, help_text)

### TO:DO

# function /setdailygoals

#functiom /trackdailygoals - automatic trigger after 9 p.m

#function /visualizeprogress - will send a chart of daily progress


bot.polling(non_stop=True)