#Line.py
def handle_message(event):
    
    if mtext == "SetFace" and status == 0:
            
            status = 1
            reply input name string
            status = 2

    elif status == 2: #recieving setFace's name
            
            reply notification put face
            enable = 0
            try:
                turnoff recognize
            except:
                print("no regcon subprocess opened")

            try:
                turnoff webcam
            except:
                print("no webcam subprocess opened")

            line_bot_api.push_message(userid, TextSendMessage(mtext + setface(mtext)))

            status = 0
            enable = 1
            sub = subprocess.Popen("exec python3 " + Reg_path, shell = True)

#create_data.py
import cv2
import numpy

def setface(name):

    mkdir name folder
    set classifier
    open camera
    sample 100 photo
    using numpy to train model
    add name to member.txt
    save model as .yml