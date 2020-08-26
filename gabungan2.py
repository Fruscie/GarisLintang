import numpy as np
import time
import RPi.GPIO as GPIO
import cv2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MKiri1 = 17
MKiri2 = 27
MKanan1 = 19
MKanan2 = 26
servoPIN1 = 21
servoPIN2 = 20

GPIO.setup(MKiri1, GPIO.OUT)
GPIO.setup(MKiri2, GPIO.OUT)
GPIO.setup(MKanan1, GPIO.OUT)
GPIO.setup(MKanan2, GPIO.OUT)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

ServoAngkat = 80
ServoCapit = 160
ServoBuka = 90
ServoTurun =35

ServoArm = GPIO.PWM(servoPIN1, 50) # GPIO 20 for PWM with 20Hz
ServoArm.start(0) # Initialization
ServoGrip = GPIO.PWM(servoPIN2, 50) # GPIO 21 for PWM with 20Hz
ServoGrip.start(0) # Initialization

mkiri1=GPIO.PWM(MKiri1, 100)
mkiri2=GPIO.PWM(MKiri2, 100)
mkanan1=GPIO.PWM(MKanan1, 100)
mkanan2=GPIO.PWM(MKanan2, 100)

def Servo(kondisi, angle):
    if kondisi == 'Capit':
        servopin = servoPIN1
        ServoP = ServoArm
    elif kondisi == 'Angkat':
        servopin = servoPIN2
        ServoP = ServoGrip
    duty = angle / 18 + 2
    GPIO.output(servopin, True)
    ServoP.ChangeDutyCycle(duty)
    time.sleep(2)
    GPIO.output(servopin, False)
  
def AwalServo():
    Servo('Capit',ServoCapit)
    Servo('Angkat',ServoAngkat)

def Motor(gerak,waktu):
    if gerak == "maju":
        print("Maju Selama " + str(waktu) + " Detik")
        mkiri1.start(30)
        mkanan1.start(30)
        time.sleep(waktu)

    elif gerak == "mundur":
        print("Mundur Selama " + str(waktu) + " Detik")
        mkiri2.start(30)
        mkanan2.start(30)
        time.sleep(waktu)

    elif gerak == "kiri":
        print("Kiri Selama " + str(waktu) + " Detik")
        mkiri2.start(30)
        mkanan1.start(30)
        time.sleep(waktu)
        
    elif gerak == "kanan":
        print("Kanan Selama " + str(waktu) + " Detik")
        mkiri1.start(30)
        mkanan2.start(30)
        time.sleep(waktu)
        
    mkiri1.start(0)
    mkiri2.start(0)
    mkanan1.start(0)
    mkanan2.start(0)

   
def Gerak(kondisi):
    print(kondisi)
    if kondisi == "Biru":
        Motor('maju', 1)
        print('Ambil Benda Biru')
        Servo('Capit', ServoBuka)
        Servo('Angkat', ServoTurun)
        AwalServo()
        Motor('mundur',0.5)
        Motor('kiri', 0.7)
        time.sleep(1)
        print('Taruh Benda')
        Servo('Angkat', ServoAngkat)
        Servo('Capit', ServoBuka)
##        Servo('Angkat', ServoAngkat)
        Servo('Capit', ServoCapit)
        Motor('kanan', 0.7)
        Motor('mundur', 0.5)

    elif kondisi == "Merah":
##        Motor('maju',0.8)
        print('Ambil Benda Merah')
##        Servo('Capit',ServoBuka)
##        Servo('Angkat',ServoTurun)
##        AwalServo()
##        Motor('mundur',0.5)
##        Motor('kiri',0.8)
##        time.sleep(1)
##        print('Taruh Benda')
##        Servo('Angkat',ServoTurun)
##        Servo('Capit',ServoBuka)
##        Servo('Angkat',ServoAngkat)
##        AwalServo()
##        Motor('kanan',0.8)
##        time.sleep(0.5)
##        Motor('mundur',0.6)

    elif kondisi == "Hijau":
##        Motor('maju',1)
        print('Ambil Benda Hijau')
##        Servo('Capit',ServoBuka)
##        Servo('Angkat',ServoTurun)
##        AwalServo()
##        Motor('mundur',0.5)
##        Motor('kiri',0.8)
##        time.sleep(1)
##        print('Taruh Benda')
##        Servo('Angkat',ServoTurun)
##        Servo('Capit',ServoBuka)
##        Servo('Angkat',ServoAngkat)
##        AwalServo()
##        Motor('kanan',0.7)
##        Motor('mundur',0.6)
        
    print('awal')
    cb = 0
    cg = 0
    cr = 0

def Kotakin(warna,img,WarnaKotak,label):
    contours, hierarchy = cv2.findContours(warna, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 1000):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), WarnaKotak, 2)
            cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, WarnaKotak)

def main():
    global Warna,i
    Warna = ""
    i = 0
    AwalServo()
    cap=cv2.VideoCapture(0)
    while(1):
        _, img = cap.read()
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        red_lower = np.array([136,87,111],np.uint8)
        red_upper = np.array([180,255,255],np.uint8)

        blue_lower = np.array([99,115,120],np.uint8)
        blue_upper = np.array([110,255,255],np.uint8)

        green_lower = np.array([25,52,72],np.uint8)
        green_upper = np.array([102, 255, 255],np.uint8)
    
        yellow_lower = np.array([22,60,200],np.uint8)
        yellow_upper = np.array([60,255,255],np.uint8)
        
        red= cv2.inRange(hsv, red_lower, red_upper)
        blue= cv2.inRange(hsv,blue_lower,blue_upper)
        green= cv2.inRange(hsv,green_lower,green_upper)
        yellow= cv2.inRange(hsv,yellow_lower,yellow_upper)
        
        cr= cv2.countNonZero(red)
        cb= cv2.countNonZero(blue)
        cg= cv2.countNonZero(green)
        cy= cv2.countNonZero(yellow)
        
        totalwarna=cb+cg+cr
        
        if totalwarna >= 1200:
            if i > 15 :
                Gerak(Warna)
                i = 0
            else:
                if cr>cb and cr>cg:
                    Warna = "Merah"
                    WarnaKotak = (0,0,255)
                    Kotakin(red,img,WarnaKotak,"Warna Merah")

                elif cb>cr and cb>cg:
                    Warna = "Biru"
                    WarnaKotak = (255, 0,0)
                    Kotakin(blue,img,WarnaKotak,"Warna Biru")

                elif cg>cr and cg>cb:
                    Warna = "Hijau"
                    WarnaKotak = (0, 255, 0)
                    Kotakin(green,img,WarnaKotak,"Warna Hijau")
                i += 1
        else:
                       
            print("Tidak Terdeteksi")

        cv2.imshow("Color Tracking",img)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            ServoArm.stop()
            ServoGrip.stop()
            GPIO.cleanup()
            break

if __name__ == "__main__":
    main()
    