try:
	import telebot
	import yt_dlp
	from telebot import types
except:
	import os
	os.system('pip install yt-dlp')
	os.system('pip install pyTelegramBotAPI')
	
token = input('Enter Your Token : ')
bot = telebot.TeleBot(token)

def download_facebook_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info_dict)
        return video_file


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ke = types.InlineKeyboardMarkup()
    btni = types.InlineKeyboardButton(text="DEv", url="https://t.me/mrfa0gh")
    ke.add(btni)
    bot.reply_to(message, "Send FB Video url",reply_markup=ke)

@bot.message_handler(func=lambda message: True)
def download_and_send_video(message):
    url = message.text
    bot.reply_to(message, "Downloading")
    
    try:
        video_path = download_facebook_video(url)
        with open(video_path, 'rb') as video:
            bot.send_video(message.chat.id, video,caption='Done By @Mrfa0gh')
    except Exception as e:
        bot.reply_to(message, f"Error in DW: {e}")

print('Bot works go to bot then do /start')
bot.polling()
