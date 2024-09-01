import telebot
import logging
from conf import TELEGRAM_API_KEY
from commands import CommandHandler
bot = telebot.TeleBot(TELEGRAM_API_KEY)

if __name__ == "__main__":
    command_handler = CommandHandler(bot)    
        
    bot.polling(none_stop = True)