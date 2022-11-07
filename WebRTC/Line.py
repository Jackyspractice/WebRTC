#Line
from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import signal

from pyngrok import ngrok
from create_data import setface
from PWM import *
from schedule import *
from build_template import *


import time
import subprocess

import logging
import argparse
logger = logging.getLogger("pc")
app = Flask(__name__)
Reg_path = os.path.abspath("Regcon.py")
server_path = os.path.abspath("server.py")

#tokens
line_bot_api = LineBotApi('hy1MPmID80D6fM0jPXOKEjKO7MzZFOAiqHgLVlE1yBWeNHwYlPxDPxLqUBd4zm/XyOE/89iMmvZ69fnekdps9Y9hgbOr3Mvmi0nkp/jDlIydLrhC0k1A7RwL7QMQEkp6LzX7WkEEF4BQZV6/OOqypgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('39e09da5ec6ccdc24b2848ed3b055336') #Channel secret
ngrok_token = "2EFlxQQDpreqVGMuQVTtTepMzHB_7Px3VmMDjcQxgLoDH7Ync"

webcam_URL = None
status = 0 #[empty, 0], [occupy, 1], [input facename, 2]...elses check FSM
sub = None #for Regcon.py
sub_webcam = None #for server.py
set = set_schedule()
setlist = []

emoji1 = [
    {
        "index": 0,
        "productId": "5ac21c46040ab15980c9b442",
        "emojiId": "008"
    }
]

class parser:

    args = None

    def set_logging_level(self):

        if args.verbose:
            logging.basicConfig(level = logging.DEBUG)
            print("Debuge MODE")
        else:
            logging.basicConfig(level = logging.INFO)
            print("INFO MODE")

    def set_parser(self):

        global args

        parser = argparse.ArgumentParser(
            description = "Line"
        )

        parser.add_argument("--verbose", "-v", action = "count")

        args = parser.parse_args()

        self.set_logging_level()

@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:

        handler.handle(body, signature)

    except InvalidSignatureError:

        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):

    global status, sub, sub_webcam
    
    if isinstance(event.message, TextMessage):

        if sub_webcam != None:
            sub_webcam.kill()
            #os.kill(sub_webcam.pid, signal.SIGTERM)
            print("exit server.py")
            sub_webcam = None
            sub = subprocess.Popen("exec python3 " + Reg_path, shell = True)

        mtext = event.message.text
        userid = event.source.user_id
        #groupid = event.source.group_id

        if status == 1:

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Channel is occupy, please wait...", emojis = emoji1))

        elif mtext == "Webcam" and status == 0:

            status = 1
            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Connecting Webcam...", emojis = emoji1))

            #webcam_URL = get_ngrok_URL()

            try:
                sub.kill()
                #os.kill(sub.pid, signal.SIGTERM)
                print("exit regcon.py")
                sub = None
            except:
                print("no subprocess opened")

            sub_webcam = subprocess.Popen("exec python3 " + server_path, shell = True)

            time.sleep(1)

            if (type(webcam_URL) == type("string")):

                line_bot_api.push_message(userid, TextSendMessage(webcam_URL))

            else:

                line_bot_api.push_message(userid, TextSendMessage("$Connection Fail, Please retry later.", emojis = emoji1))

            #open_webcam()

            status = 0

        elif mtext == "OpenBox" and status == 0:
            
            status = 1

            try:
                sub.kill()
                #os.kill(sub.pid, signal.SIGTERM)
                print("exit regcon.py")
                sub = None
            except:
                print("no regcon subprocess opened")

            line_bot_api.reply_message(event.reply_token, Carousel_Box())      

            status = 100
    
        elif mtext == "SetFace" and status == 0:
            
            status = 1

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$input your name, before setting face...", emojis = emoji1))

            status = 2

        elif mtext == "Set_Schedule" and status == 0:

            status = 1

            try:
                #sub.kill()
                os.kill(sub.pid, signal.SIGTERM)
                print("exit regcon.py")
                sub = None
            except:
                print("no regcon subprocess opened")
            
            list = set.find_all_people()

            if list == -1:
                line_bot_api.reply_message(event.reply_token, TextSendMessage("No any person exist!"))
            else:
                line_bot_api.reply_message(event.reply_token, Namelist(list))


            status = 3

        elif mtext == "Delete" and status == 0:

            status = 1

            try:
                sub.kill()
                #os.kill(sub.pid, signal.SIGTERM)
                print("exit regcon.py")
                sub = None
            except:
                print("no regcon subprocess opened")
            
            list = set.find_all_people()

            if list == -1:
                line_bot_api.reply_message(event.reply_token, TextSendMessage("No any person exist!"))
                status = 0
            else:
                line_bot_api.reply_message(event.reply_token, Namelist(list))
                status = 6

        elif mtext == "Show_Schedule" and status == 0:

            status = 1
            
            line_bot_api.reply_message(event.reply_token, TextSendMessage(set.All()))

            status = 0

        elif status == 6: # delete person

            line_bot_api.reply_message(event.reply_token, TextSendMessage(set.delete_person(mtext)))
            status = 0
            sub = subprocess.Popen("exec python3 " + Reg_path, shell = True)

        elif status == 3: # schedule who

            setlist.clear()
            setlist.append(mtext)
            line_bot_api.reply_message(event.reply_token, Carousel_Weekday())

            status = 4

        elif status == 4: # schedule weekday

            setlist.append(mtext)
            line_bot_api.reply_message(event.reply_token, Carousel_Box())

            status = 5

        elif status == 5: # schedule whichBox

            setlist.append(mtext)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(set.set(setlist[0], setlist[1], setlist[2])))

            status = 0
            sub = subprocess.Popen("exec python3 " + Reg_path, shell = True)

        elif status == 2: #recieving setFace's name
            
            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Having U'r face in front of Camera for 5 Sec when light is on...", emojis = emoji1))

            try:
                sub.kill()
                #os.kill(sub.pid, signal.SIGTERM)
                print("exit regcon.py")
                sub = None
            except:
                print("no regcon subprocess opened")

            try:
                sub_webcam.kill()
                #os.kill(sub_webcam.pid, signal.SIGTERM)
                print("exit server.py")
                sub_webcam = None
            except:
                print("no webcam subprocess opened")


            line_bot_api.push_message(userid, TextSendMessage(mtext + setface(mtext)))

            status = 0
            sub = subprocess.Popen("exec python3 " + Reg_path, shell = True)

        elif status == 100:
            
            number = mtext

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Opening Box for you...", emojis = emoji1))
            
            try:
                pwm = PWM_Control()
                
                pwm.initial()
                pwm.active(number)
            except:
                print("PWM Error!")

            sub = subprocess.Popen("exec python3 " + Reg_path, shell = True)
            status = 0

        else:

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Shut Up!", emojis = emoji1))

def open_port():

    global webcam_URL

    print("open ngrok")
    ngrok.set_auth_token(ngrok_token)
    http_tunnel_Line = ngrok.connect(addr = 5000, bind_tls = True)
    print("Line-------------------->" + http_tunnel_Line.public_url)
    http_tunnel_Server = ngrok.connect(addr = 8080, bind_tls = True)
    print("Server-------------------->" + http_tunnel_Server.public_url)

    webcam_URL = http_tunnel_Server.public_url

if __name__ == '__main__':

    sub = subprocess.Popen("exec python3 " + Reg_path, shell = True)
    open_port()
    app.run()
