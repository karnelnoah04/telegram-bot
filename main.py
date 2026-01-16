import telebot
import time

BOT_TOKEN = "8577339895:AAHfRns-_MpRO35XJGnOcTgYKN9RrFVpvbw"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Bot AirdropInfo aktif 24 jam!")

@bot.message_handler(commands=['airdrop'])
def airdrop(message):
    bot.reply_to(message, "🔥 Info airdrop akan update otomatis")

print("Bot running...")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(5)
