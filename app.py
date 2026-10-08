import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get('BOT_TOKEN', 'موت_هنا')
bot = telebot.TeleBot(TOKEN)

YEAR_CODES = [
    "Hjk2356j", "455hnm0", "Zx5091oy", "bcc",
    "Gak1018uq", "Ui20067ytr", "2300gasnq"
]

MONTH_CODES = [
    "Jn6021sak", "000gawlbv", "34g34kjaer",
    "5qoognmay", "Q232bnou5", "jjnb491300"
]

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك لتفعيل كورسات التداول")

@bot.message_handler(func=lambda message: True)
def check_code(message):
    user_code = message.text.strip()
    
    if user_code in YEAR_CODES or user_code in MONTH_CODES:
        bot.reply_to(message, "✅ تم تفعيل الاشتراك بنجاح")
        bot.send_message(message.chat.id, "📈 **المقدمة والكورس الأول:** خطوة بخطوة نحو الاحتراف.")
        bot.send_message(message.chat.id, "🎯 **تعليمات القنوات:** قواعد هامة لضمان العمل والسوق تماماً.")
        
        course_3_text = (
            "📉 **الكورس الثالث:** شرح الارتدادات خطوة بخطوة.\n\n"
            "هذه النقاط مجرد أدوات، ولكن الأهم أن تكون فهماً لطريقة العمل والسوق تماماً ⚠️\n\n"
            "هذا الكود تم تجهيزه بعناية ليشرح لك كل ما فاتك لتبدأ بقوة.\n\n"
            "للتواصل مع المشرف ومتابعة أي استفسار 👇"
        )
        bot.send_message(message.chat.id, course_3_text)
    else:
        bot.reply_to(message, "❌ رمز غير صحيح، يرجى التحقق وإعادة المحاولة.")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
