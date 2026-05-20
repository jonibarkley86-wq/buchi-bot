import telebot
import datetime
import random

# የቦት ቶከን
BOT_TOKEN = "8405392398:AAFcN5SpNwH3rRkHLFUZgPyEQ9LUq94UfzM"
bot = telebot.TeleBot(BOT_TOKEN)

def get_greeting():
    # የኢትዮጵያ ሰዓት (UTC+3)
    hour = (datetime.datetime.utcnow().hour + 3) % 24
    
    if 5 <= hour < 12:
        greetings = [
            "እንዴት አደርሽ የኔ ልዕልት! ቆንጆ ጠዋት ይሁንልሽ፣ ምን ልታዘዝ? 😍",
            "ደህና አደርሽ የኔ ውድ! የዛሬው ቀንሽ የተባረከ ይሁን፣ ምን ላድርግልሽ? ❤️",
            "ጠዋትሽ እንደ ፀሐይ ይደምቅ የኔ ቆንጆ፣ ምን ልታዘዝልሽ? 💖",
            "የጠዋት አበባዬ፣ እንዴት አደርሽልኝ? ምን ላምጣልሽ? 🌹"
        ]
    elif 12 <= hour < 18:
        greetings = [
            "እንዴት ዋልሽ የኔ ትንሽዬ መልአክ? ምን ልታዘዝልሽ? 😍",
            "የኔ ቆንጆ እንዴት ዋልሽልኝ? ዛሬ ምን ላግዝሽ? ❤️",
            "የቀኑን ውሎሽን አሳምርልሽ፣ ምን ላድርግልሽ የኔ ውድ? 💖",
            "የቀኔ ብርሃን፣ እንዴት ዋልሽ? ምን ላምጣልሽ? ☀️"
        ]
    else:
        greetings = [
            "እንዴት አመሸሽ የኔ አበባ! ዛሬ ምን ላምጣልሽ? 😍",
            "የማታው ውበት የኔ ፍቅር፣ እንዴት አምሽተሻል? ምን ልታዘዝ? ❤️",
            "እንዴት አመሸሽ የኔ መልአክ! ምን ላድርግልሽ? 💖",
            "የማታው ኮከቤ፣ እንዴት አመሸሽ? ምን ላድርግልሽ? ⭐"
        ]
    return random.choice(greetings)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, get_greeting())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # መጀመሪያ ሰላምታውን ይላክ
    bot.reply_to(message, get_greeting())
    # ቪዲዮውን ለማምጣት የሚል መልእክት
    bot.send_message(message.chat.id, "ቪዲዮሽን እየበረርኩ ሄጄ ላምጣ! ✈️🎁")
    
    # እዚህ ጋር የቪዲዮ ማውረጃ ኮድህን (yt-dlp) መጨመር ትችላለህ

bot.polling()
