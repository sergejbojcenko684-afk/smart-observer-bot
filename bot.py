import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет! 🤖 Бот работает!")

@bot.message_handler(commands=["status"])
def status(message):
    bot.reply_to(message, "Бот запущен и готов к работе.")

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message, "Доступные команды: /start, /status, /help")

bot.infinity_polling()
