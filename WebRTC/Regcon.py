import cv2
import time
from PWM import *

cap = cv2.VideoCapture(0)

class Recognize:

    def whoareu(self):
        
        global cap

        model = cv2.face.LBPHFaceRecognizer_create()
        model.read('faces_LBPH.yml')
        f = open('member.txt', 'r')  #讀入模型
        names = f.readline().split(',')  #讀入姓名存於串列
        face_cascade = cv2.CascadeClassifier("/home/jacky/Desktop/WebRTC/WebRTC/haarcascade_frontalface_alt2.xml")
        #face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
        #cap = cv2.VideoCapture(0)
        #cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

        timenow = time.time()  #取得現在時間數值
        
        if (cap.isOpened() == False):
            return False, "CamERROR"
        
        '''
        while(cap.isOpened()):  #cam開啟成功
            print("Starting Regconface, put U'r face on screen", end = '\r')
            count = 4 - int(time.time() - timenow)  #倒數計時5秒
            ret, img = cap.read()
            if ret == True:
                #imgcopy = img.copy()  #複製影像
                #cv2.putText(imgcopy, str(count), (200,400), cv2.FONT_HERSHEY_SIMPLEX, 15, (0,0,255), 35)  #在複製影像上畫倒數秒數
                #cv2.imshow("frame", imgcopy)  #顯示複製影像
                if count == 0:  #倒數計時結束
                    cv2.imwrite("media/tem.jpg", img)  #將影像存檔
                    break
        #cap.release()  #關閉cam
        #cv2.destroyAllWindows()
        '''

        sum = 0
        times = 0
        while(cap.isOpened()):  #cam開啟成功
            #print("Starting Regconface, put U'r face on screen", end = '\r')

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)


            #img = cv2.imread("media/tem.jpg")
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 3)

            for (x, y, w, h) in faces:
                #img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                print("Starting Regconface, put U'r face on screen")
                face_img = cv2.resize(gray[y: y + h, x: x + w], (400, 400))  #調整成訓練時大小
                val = model.predict(face_img)
                sum += val[1]
                times += 1
                if times == 2: 
                    break

            time.sleep(0.2)

            if times == 2:
                try:
                    if sum / times < 35:  #辨識成功，顯示登入訊息
                        print('\n歡迎 ' + names[val[0]] + ' 登入！相似度:', 100 - sum / times)

                        #PWM Here
                        #------------------------------------------------

                        print("opening box for you...")

                        #------------------------------------------------


                        return True, "Success"
                    else:
                        print('\n抱歉！你不是會員，無法登入！')
                        return False, "Sorry Not U"
                except:
                    print('\n辨識時產生錯誤！')
                    return False, "RegERROR"
            
            #print("\n沒有人啊?")

    def anyone(self):

        global cap
        
        detector = cv2.CascadeClassifier("/home/jacky/Desktop/WebRTC/WebRTC/haarcascade_frontalface_default.xml")
        #detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        if (cap.isOpened() == False):
            return False, "CamERROR"

        num = 0
        while(1):

            print("Waiting a person to show up!", end = '\r')
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x, y, w, h) in faces:

                num += 1

            if num != 0:

                print("\nSomeone shows up! Start Recognizing...")

                return 1
            
            else:
                time.sleep(0.2)
            
        #cap.release()  #關閉cam
        #cv2.destroyAllWindows()

if __name__ == "__main__":

    Reg = Recognize()
    
    while 1:

        if Reg.anyone():

            Reg.whoareu()
