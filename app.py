import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get('BOT_TOKEN', 'موت_هنا')
bot = telebot.TeleBot(TOKEN)

YEAR_CODES = [
    "gaihf38296Y491", "Tidbh648Y702", "kloqrz91Y384", "vnmx732Y516", "wqeplm88Y625", 
    "zxcvbn43Y109", "ytrewq99Y837", "poiuyt12Y450", "mnbvcx67Y291", "lkjhgf55Y783", 
    "asdfgh34Y612", "ZXcvbn88Y904", "QweRty11Y348", "PlMkoI77Y560", "ZsxCdE90Y213", 
    "BnhYgt44Y879", "VfrCde22Y135", "XswAqa66Y694", "MkoIuj33Y481", "NjiUhy55Y726", 
    "HbgTfr88Y390", "YhnUjm99Y512", "EdcRfv11Y804", "TgbYhn77Y267", "UjmIko44Y945", 
    "IopLkj22Y178", "OijUhy66Y631", "PlkMnb88Y409", "AswQaz33Y852", "SdeWsa55Y197", 
    "DfrEdc77Y724", "FgtRfv99Y386", "GhyTgb22Y513", "HjuYhn44Y968", "JklUjm66Y241", 
    "KopIko88Y605", "LoiPlo11Y473", "MnbAsw33Y819", "BvcSde55Y154", "CxzDfr77Y932", 
    "ZasFgt99Y280", "XswGhy22Y674", "CdeHju44Y418", "VfrJkl66Y893", "BgtKop88Y307", 
    "NhyLoi11Y561", "MjuMnb33Y749", "KopBvc55Y128", "LoiCxz77Y685", "UjmZas99Y456"
]

MONTH_CODES = [
    "bvcxz781M903", "lkjhg920M417", "rewqas34M682", "poiuy651M159", "mnbvc873M740", 
    "asdfg219M325", "zxcvb648M816", "ytrew109M594", "lkjuy772M203", "mnkji334M668", 
    "PlkMko55M902", "QazWsx88M431", "EdcRfv22M756", "TgbYhn99M182", "UjmIko33M614", 
    "IopLkj66M398", "ZsxCde44M827", "BnhYgt77M250", "VfrCde11M539", "XswAqa33M971", 
    "MkoIuj88M146", "NjiUhy22M683", "HbgTfr55M319", "YhnUjm77M805", "EdcRfv44M492", 
    "TgbYhn11M723", "UjmIko66M158", "IopLkj99M384", "OijUhy33M960", "PlkMnb55M241", 
    "AswQaz77M617", "SdeWsa22M839", "DfrEdc44M105", "FgtRfv66M582", "GhyTgb88M396", 
    "HjuYhn11M741", "JklUjm33M209", "KopIko55M653", "LoiPlo77M894", "MnbAsw99M412", 
    "BvcSde22M175", "CxzDfr44M938", "ZasFgt66M304", "XswGhy88M567", "CdeHju11M821", 
    "VfrJkl33M149", "BgtKop55M760", "NhyLoi77M283", "MjuMnb99M518", "UjmZas22M694"
]

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "أهلاً بك! للاشتراك، يرجى تزويدنا باسمك ورقمك للتواصل عبر الواتساب مع المشرف الثاني ليمنحك كود التفعيل.\n\n"
        "بعد حصولك على الكود، قم بإرساله هنا لتفعيل اشتراكك فوراً."
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def check_code(message):
    user_code = message.text.strip()
    
    if user_code in YEAR_CODES or user_code in MONTH_CODES:
        success_text = (
            "🎉 تم تفعيل الكود بنجاح! إليك روابط كورساتك:\n\n"
            "الكورسات :\n\n"
            "📊 الكورس 1 - التحليل الفني: https://t.me/c/4358617248/4\n\n"
            "📉 الكورس 2 - القمم والقيعان: https://t.me/c/4358617248/5\n\n"
            "🎯 الكورس 3 - نقطة دخول لصفقات: https://t.me/c/4358617248/6"
        )
        bot.reply_to(message, success_text)
    else:
        bot.reply_to(message, "❌ رمز غير صحيح، يرجى التحقق من الكود وإعادة المحاولة.")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
