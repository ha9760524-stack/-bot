import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get('BOT_TOKEN', 'ضع_توكن_البوت_هنا')
bot = telebot.TeleBot(TOKEN)

YEAR_CODES = [
    "Hjk2356j", "455hnm0", "Zx5091oy", "bcc549hj7", "995ghj4",
    "Gak1018uq", "Ui20067ytr", "2300gasnq", "Ytr81005dfy", "541hgatr8"
]

MONTH_CODES = [
    "Jn6021sak", "000gawlbv", "34g34kjaer", "1515gvzx23",
    "5qoognmay", "Q232bnou5", "jjnb491300", "Rth402155"
]

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في بوت اشتراكات كورسات التداول 📉.\nالرجاء إرسال كود الاشتراك الخاص بك لتفعيل الخدمة واستلام جميع الكورسات.")

@bot.message_handler(func=lambda message: True)
def check_code(message):
    user_code = message.text.strip()
    
    if user_code in YEAR_CODES or user_code in MONTH_CODES:
        bot.reply_to(message, "✅ **تم تفعيل الاشتراك بنجاح!**\nإليك محتوى الكورسات والشروحات الخاصة بك 📊:", parse_mode='Markdown')
        
        bot.send_message(message.chat.id, "📈 **الكورس الأول: شرح التحليل الفني**")
        bot.send_message(message.chat.id, "🎯 **الكورس الثاني: شرح نقطة دخول لصفقات**")
        
        course_3_text = (
            "📉 **الكورس الثالث: شرح القمم والقيعان والارتدادات**\n\n"
            "‼️ يا خوان أعرف لسوق سمارتي فقط، بس أهم شي إنك فاهم طريقة الكورسات، "
            "وإذا ما فهمتها تواصل مع المشرف يشرح لك اللي ما فهمته، أهم شي إنك تتعلم.\n\n"
            "للتواصل مع المشرف 👈🏻 @Trz179"
        )
        bot.send_message(message.chat.id, course_3_text, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ **الكود غير صحيح أو منتهي.** تأكد من الكود وأعد محاولة إرساله بشكل صحيح.", parse_mode='Markdown')

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
