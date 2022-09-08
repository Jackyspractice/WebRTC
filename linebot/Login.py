#Line
from flask import Flask
from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from RSA_File import Write_and_Export

app = Flask(__name__)

#token
line_bot_api = LineBotApi('AeXTgftCbK2BDogofsoXbMObgU3TaL1fCMtuxtU94u7MlFkIeEXoNNR4RGIi9CdYC4vaq3lp4/SnBjWGcHLhMfUKS3qvahcB25af0td3K8xEckO48OC+UXuJMkXW75yfaVXE84tyZ5JaprzbglFsEQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2d77a86e124cc8b38d427613455d11ab') #Channel secret

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

            information = start_Login(mtext)

            if (type(information) == type("string")):

                line_bot_api.push_message(userid, TextSendMessage(information))

            else:

                msg = store_information(information)

                line_bot_api.push_message(userid, TextSendMessage(msg))

                information.clear()

        elif mtext == 'help' or mtext == 'Help':

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$You don't need help\nTo Sign Up, Press Sign Up botton\nYour password will use RSA1024bits to Encrypt!", emojis = emoji1))
            status = 0

        elif mtext == 'list' or mtext == 'List':
            
            lists = Write_and_Export().export()
            if (lists == None):
                line_bot_api.reply_message(event.reply_token, TextSendMessage("To Sign Up, Press Sign Up botton $", emojis = emoji2))
            else:

                lists_user_msg = "*****Account*****\n"

                for i in range (0, len(lists)):

                    lists_user_msg += "\U0001F449 " + lists[i].user + " \U0001F448" +'\n'

                lists_user_msg += "****End of List****"

                line_bot_api.reply_message(event.reply_token, TextSendMessage(lists_user_msg))

            status = 0
            line_bot_api.push_message(userid, TextSendMessage("To Sign Up, Press Sign Up botton $", emojis = emoji2))

        elif mtext == 'SignUp' or mtext == 'S':

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Please input Your\nStudentID%Password%\nEx:10828152%password%", emojis = emoji1))
            

        elif len(mtext) >= 12 and mtext[len(mtext)-1] == '%':
            
            size = len(mtext)
            person = (Student(mtext[0 : 8], mtext[9 : size - 1]))
            print(person)
            Write_and_Export().store(person)
            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Sign Up Successfully", emojis = emoji1))
        
        else:

            line_bot_api.reply_message(event.reply_token, TextSendMessage("$Shut Up!", emojis = emoji1))
            status = 0

if __name__ == '__main__':

    app.run()
