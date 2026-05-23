import telebot
import datetime
import random
import yt_dlp
import os

# የቦት ቶከን
bot = telebot.TeleBot("8708361571:AAEZlQD8WWj--90lWrgNsINTKKe8lP4Juag")

@bot.message_handler(func=lambda message: message.text and message.text.startswith('http'))
def handle_link(message):
    chat_id = message.chat.id
    msg = bot.reply_to(message, "🚀 ቪዲዮውን እያወረድኩ ነው፣ ጥቂት ጠብቂኝ...")
    
    try:
        # ለሁሉም አይነት ሊንኮች (ቴሌግራምን ጨምሮ) የሚሆን ማውረጃ
        ydl_opts = {
            'format': 'best', 
            'outtmpl': f'video_{chat_id}.mp4', 
            'noplaylist': True,
            'quiet': True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([message.text])
        
        video_path = f'video_{chat_id}.mp4'
        with open(video_path, 'rb') as video:
            bot.send_video(chat_id, video)
        
        bot.send_message(chat_id, "ይሄው የኔ ልዕልት! 😍")
        os.remove(video_path)
        
    except Exception:
        bot.reply_to(message, "ይህንን ሊንክ ማውረድ አልቻልኩም፣ ሌላ ሞክሪ! 😢")

bot.infinity_polling()
