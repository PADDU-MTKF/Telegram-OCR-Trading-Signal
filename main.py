from dotenv import load_dotenv
import requests as req
import os
import telebot
import time
import sys

# ************************************************************************************************
load_dotenv()

API_KEY = os.getenv('API_KEY')
OCR_KEY = os.getenv('OCR_KEY')
CID = os.getenv('CID')
FROM_GID = os.getenv('FROM_GID')
TO_GID = os.getenv('TO_GID')
CID_DEV = CID


bot = telebot.TeleBot(API_KEY)


req_txt = ['Precio', 'Stop Loss', 'Take Profit']
# ************************************************************************************************


def permission(message):
    if str(message.chat.id) == FROM_GID:
        return True
    return False


def get_img(message):
    file_id = message.photo[-1].file_id
    file = bot.get_file(file_id)
    link = 'https://api.telegram.org/file/bot' + API_KEY + '/' + file.file_path
    return link


def ocr(link):
    data = req.get(
        f"https://api.ocr.space/parse/imageurl?apikey={OCR_KEY}&url={link}&language=eng&detectOrientation=True&filetype=JPG&OCREngine=1&isTable=True&scale=True")
    data = data.json()
    if data['IsErroredOnProcessing'] == False:
        mess = data['ParsedResults'][0]['ParsedText']

    else:
        mess = "Something went wrong, please try again later"

    return mess


def check_data(mess):
    if req_txt[0] in mess and req_txt[1] in mess and req_txt[2] in mess:
        mess = mess.split()
        buy = stoploss = ''
        for each in mess:
            if each.lower() == 'precio':
                buy = mess[mess.index(each)+1]
            elif each.lower() == 'loss':
                stoploss = mess[mess.index(each)+1]

        if float(stoploss.strip()) > float(buy.strip()):
            action = 'Sell'
        else:
            action = 'Buy'
        return(f"{action} XAUUSD at {buy}\nStop loss at {stoploss}")

    return False

# ************************************************************************************************


@bot.message_handler(func=permission, content_types=['photo'])
def extract(message):
    # print(message.chat.id)
    if message.photo == None:
        return
    else:
        link = get_img(message)
        mess = ocr(link)
        result = check_data(mess)

        if result != False:
            bot.send_message(TO_GID, result)
        else:
            pass


while True:
    time.sleep(0.002)
    try:
        print("The Bot is running ......\n\n")
        bot.polling(non_stop=True, interval=1)

    except Exception as e:
        try:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            t = 'Error :- ' + str(exc_type) + '\nFile  :- ' + str(
                fname) + '\nLine  :- ' + str(exc_tb.tb_lineno)
            print(t)
            bot.send_message(CID_DEV, t)

            print('Retrying .....\n\n')
            time.sleep(5)

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            t = 'Error :- ' + str(exc_type) + '\nFile  :- ' + str(
                fname) + '\nLine  :- ' + str(exc_tb.tb_lineno)
            print(t)
