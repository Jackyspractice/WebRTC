#Line
from flask import Flask
from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from server import open_webcam, get_ngrok_URL
from pyngrok import ngrok
from PWM import *

app = Flask(__name__)

#token
line_bot_api = LineBotApi('hy1MPmID80D6fM0jPXOKEjKO7MzZFOAiqHgLVlE1yBWeNHwYlPxDPxLqUBd4zm/XyOE/89iMmvZ69fnekdps9Y9hgbOr3Mvmi0nkp/jDlIydLrhC0k1A7RwL7QMQEkp6LzX7WkEEF4BQZV6/OOqypgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('39e09da5ec6ccdc24b2848ed3b055336') #Channel secret
ngrok_token = "2EFlxQQDpreqVGMuQVTtTepMzHB_7Px3VmMDjcQxgLoDH7Ync"

emoji1 = [
    {
        "index": 0,
        "productId": "5ac21c46040ab15980c9b442",
        "emojiId": "008"
    }
]
emoji2 = [
    {
        "index": 33,
        "productId": "5ac21e6c040ab15980c9b444",
        "emojiId": "020"
    }
]

class Student:

    def __init__(self, user = None, passwd = None):
        self.user = user
        self.passwd = passwd

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
    
    if isinstance(event.message, TextMessage):

        mtext = event.message.text
        userid = event.source.user_id
        #groupid = event.source.group_id

        if mtext == "Webcam":

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Connecting Webcam...", emojis = emoji1))

            webcam_URL = get_ngrok_URL()
            

            if (type(webcam_URL) == type("string")):

                line_bot_api.push_message(userid, TextSendMessage(webcam_URL))

            else:

                line_bot_api.push_message(userid, TextSendMessage("$Connection Fail, Please retry later.", emojis = emoji1))

            open_webcam()


        elif mtext == "Box1":
            
            line_bot_api.reply_message(event.reply_token, TextSendMessage("Opening Box1 for you...$", emojis = emoji1))
            
            PWM = PWM_Control()
            
            PWM.initial()
            PWM.Open()
            PWM.Reset()


        elif mtext == "Box2":

            line_bot_api.reply_message(event.reply_token, TextSendMessage("Opening Box2 for you...$", emojis = emoji2))            

        elif mtext == "Set":
            
            line_bot_api.reply_message(event.reply_token, TextSendMessage("You really want to set schedule?$", emojis = emoji2))
        
        else:

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Shut Up!", emojis = emoji1))

def open_port():

    ngrok.set_auth_token(ngrok_token)
    http_tunnel = ngrok.connect(5000)

if __name__ == '__main__':

    open_port()
    app.run()
