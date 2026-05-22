import telebot
import datetime
import random
import yt_dlp
import os

bot = telebot.TeleBot("8405392398:AAFcN5SpNwH3rRkHLFUZgPyEQ9LUq94UfzM")
user_last_greeted = {}

def get_greeting(hour):
    if 5 <= hour < 12:
        return random.choice(["እንዴት አደርሽ የኔ ልዕልት! 😍", "ደህና አደርሽ የኔ ውድ! ❤️", "ጠዋትሽ እንደ ፀሐይ ይደምቅ የኔ ቆንጆ፣ ምን ልታዘዝልሽ? 💖", "የጠዋት አበባዬ፣ እንዴት አደርሽልኝ? 🌹"])
    elif 12 <= hour < 18:
        return random.choice(["እንዴት ዋልሽ የኔ ትንሽዬ መልአክ? 😍", "የኔ ቆንጆ እንዴት ዋልሽልኝ? ❤️", "የቀኑን ውሎሽን አሳምርልሽ፣ ምን ላድርግልሽ የኔ ውድ? 💖", "የቀኔ ብርሃን፣ እንዴት ዋልሽ? ☀️"])
    else:
        return random.choice(["እንዴት አመሸሽ የኔ አበባ! 😍", "የማታው ውበት የኔ ፍቅር! ❤️", "እንዴት አመሸሽ የኔ መልአክ! 💖", "የማታው ኮከቤ፣ እንዴት አመሸሽ? ⭐"])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, get_greeting((datetime.datetime.utcnow().hour + 3) % 24))

@bot.message_handler(func=lambda message: message.text.startswith('http'))
def handle_link(message):
    chat_id = message.chat.id
    # ሰላምታ በቀን አንድ ጊዜ
    if user_last_greeted.get(chat_id) != datetime.date.today():
        bot.send_message(chat_id, get_greeting((datetime.datetime.utcnow().hour + 3) % 24))
        user_last_greeted[chat_id] = datetime.date.today()
    
    msg = bot.reply_to(message, "✈️ ቪዲዮሽን እየበረርኩ ሄጄ ላምጣ፣ ጥቂት ጠብቂኝ...")
    try:
        ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4', 'noplaylist': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([message.text])
        
        with open('video.mp4', 'rb') as video:
            bot.send_video(chat_id, video)
        bot.send_message(chat_id, "ይሄው የኔ ልዕልት! 😍")
        os.remove('video.mp4')
    except Exception as e:
        bot.reply_to(message, "አልተሳካም፣ ሊንኩን እንደገና ሞክሪ! 😢")

bot.infinity_polling()
