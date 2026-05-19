import telebot
import yt_dlp
import os

# የእርስዎ ቶከን በቀጥታ ገብቷል
BOT_TOKEN = "8405392398:AAFcN5SpNwH3rRkHLFUZgPyEQ9LUq94UfzM"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🤖 Buchi Bot ዝግጁ ነው። ሊንክ ላክልኝ በፍጥነት አወርድልሃለሁ።")

@bot.message_handler(func=lambda m: True)
def handle_link(m):
    if "http" in m.text:
        msg = bot.reply_to(m, "እባክዎ ትንሽ ይጠብቁ... እየወረደ ነው...")
        try:
            ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([m.text])
            with open('video.mp4', 'rb') as v:
                bot.send_video(m.chat.id, v, caption="ይኸው ተጠናቀቀ!")
            os.remove('video.mp4')
            bot.delete_message(m.chat.id, msg.message_id)
        except Exception as e:
            bot.reply_to(m, f"ስህተት ተፈጥሯል: {str(e)}")
    else:
        bot.reply_to(m, "እባክዎ ትክክለኛ ሊንክ ይላኩ።")

bot.infinity_polling()