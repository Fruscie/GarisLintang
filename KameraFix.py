import cv2
import numpy as np
import time

def Gerak(kondisi):
	if kondisi == "Merah":
		print("Sukses Servo Merah")
		cb = 0
		cy = 0
		cr = 0
		print("DELAY MOTOR SERVO JALAN")
		time.sleep(1)
	elif kondisi == "Biru":
		print("Sukses Servo Biru")
		cb = 0
		cy = 0
		cr = 0
		print("DELAY MOTOR SERVO JALAN")
		time.sleep(1)
	elif kondisi == "Kuning":
		print("Sukses Servo Kuning")
		cb = 0
		cy = 0
		cr = 0
		print("DELAY MOTOR SERVO JALAN")
		time.sleep(1)

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
			if i > 7 :
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
			break

if __name__ == "__main__":
	main()
