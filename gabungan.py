import numpy as np
import time
import RPi.GPIO as GPIO
import cv2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MKiri1 = 19
MKiri2 = 26
MKanan1 = 27
MKanan2 = 17
servoPIN1 = 20
servoPIN2 = 21

GPIO.setup(MKiri1, GPIO.OUT)
GPIO.setup(MKiri2, GPIO.OUT)
GPIO.setup(MKanan1, GPIO.OUT)
GPIO.setup(MKanan2, GPIO.OUT)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

AwalAngkat = 95
AwalCapit = 100

p1 = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
p1.start(0) # Initialization
p2 = GPIO.PWM(servoPIN2, 50) # GPIO 17 for PWM with 50Hz
p2.start(0) # Initialization
mkiri1=GPIO.PWM(MKiri1, 100)
mkiri2=GPIO.PWM(MKiri2, 100)
mkanan1=GPIO.PWM(MKanan1, 100)
mkanan2=GPIO.PWM(MKanan2, 100)
def Capit(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPIN1, True)
	p1.ChangeDutyCycle(duty)
	time.sleep(2)
	GPIO.output(servoPIN1, False)

	
def Angkat(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPIN2, True)
	p2.ChangeDutyCycle(duty)
	time.sleep(2)
	GPIO.output(servoPIN2, False)

  
def AwalServo():
    Capit(AwalCapit)
    Angkat(AwalAngkat)
    p1.start(0)
    p2.start(0)

def Motor(gerak,waktu):
    if gerak == "maju":
        print('Maju')
        mkiri1.start(30)
        mkiri2.start(0)
        mkanan1.start(30)
        mkanan2.start(0)
        time.sleep(waktu)
        mkiri1.start(0)
        mkiri2.start(0)
        mkanan1.start(0)
        mkanan2.start(0)

    elif gerak == "mundur":
        print("Mundur")
        mkiri1.start(0)
        mkiri2.start(28)
        mkanan1.start(0)
        mkanan2.start(100)
        time.sleep(waktu)
        mkiri1.start(0)
        mkiri2.start(0)
        mkanan1.start(0)
        mkanan2.start(0)

    elif gerak == "kiri":
        print("Kiri")
        mkiri1.start(0)
        mkiri2.start(30)
        mkanan1.start(100)
        mkanan2.start(0)
        time.sleep(waktu)
        mkiri1.start(0)
        mkiri2.start(0)
        mkanan1.start(0)
        mkanan2.start(0)
    elif gerak == "kanan":
        print("Kanan")
        mkiri1.start(60)
        mkiri2.start(0)
        mkanan1.start(0)
        mkanan2.start(40)
        time.sleep(waktu)
        mkiri1.start(0)
        mkiri2.start(0)
        mkanan1.start(0)
        mkanan2.start(0)

   
def Gerak(kondisi):
    if kondisi == "Biru":
        Motor('maju',1)
        print('Ambil Benda Biru')
        Capit(40)
        Angkat(45)
        AwalServo()
        print("motor mundur")
        Motor('mundur',0.5)
        Motor('kiri',0.8)
        time.sleep(1)
        print('Taruh Benda')
        Angkat(45)
        Capit(40)
        Angkat(95)
        AwalServo()
        Motor('kanan',0.7)
        Motor('mundur',0.6)
        print('awal')
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
    elif kondisi == "Merah":
	Motor('maju',1)
        print('Ambil Benda Merah')
        Capit(40)
        Angkat(50)
        AwalServo()
        print("motor mundur")
        Motor('mundur',0.5)
        Motor('kiri',0.8)
        time.sleep(1)
        print('Taruh Benda')
        Angkat(45)
        Capit(40)
        Angkat(95)
        AwalServo()
        Motor('kanan',0.7)
        Motor('mundur',0.6)
        print('awal')
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
    elif kondisi == "Kuning":
	Motor('maju',1)
        print('Ambil Benda Kuning')
        Capit(40)
        Angkat(45)
        AwalServo()
        print("motor mundur")
        Motor('mundur',0.5)
        Motor('kiri',0.8)
        time.sleep(1)
        print('Taruh Benda')
        Angkat(45)
        Capit(40)
        Angkat(95)
        AwalServo()
        Motor('kanan',0.7)
        Motor('mundur',0.6)
        print('awal')
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
    cb = 0
    cy = 0
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

		blue_lower = np.array([99,115,150],np.uint8)
		blue_upper = np.array([110,255,255],np.uint8)

		yellow_lower = np.array([22,60,200],np.uint8)
		yellow_upper = np.array([60,255,255],np.uint8)
	
		red= cv2.inRange(hsv, red_lower, red_upper)
		blue= cv2.inRange(hsv,blue_lower,blue_upper)
		yellow= cv2.inRange(hsv,yellow_lower,yellow_upper)
	
		cr= cv2.countNonZero(red)
		cb= cv2.countNonZero(blue)
		cy= cv2.countNonZero(yellow)
		totalwarna=cb+cy+cr
		
		if totalwarna >= 1000:
			if i > 10 :
				Gerak(Warna)
				i = 0
			else:
				if cr>cb and cr>cy:
					Warna = "Merah"
					WarnaKotak = (0,0,255)
					Kotakin(red,img,WarnaKotak,"Warna Merah")

				elif cb>cr and cb>cy:
					Warna = "Biru"
					WarnaKotak = (255, 0,0)
					Kotakin(blue,img,WarnaKotak,"Warna Biru")

				elif cy>cr and cy>cb:
					Warna = "Kuning"
					WarnaKotak = (0, 255, 255)
					Kotakin(yellow,img,WarnaKotak,"Warna Kuning")
				i += 1
		else:
                       
			print("Tidak Terdeteksi")

		cv2.imshow("Color Tracking",img)

		if cv2.waitKey(10) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()
			p1.stop()
			p2.stop()
			GPIO.cleanup()
			break

if __name__ == "__main__":
	main()
	