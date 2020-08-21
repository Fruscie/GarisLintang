import cv2
import numpy as np
import time

def Gerak(kondisi):
	if kondisi == "Merah":
		print("Sukses Servo Merah")
		print("DELAY MOTOR SERVO JALAN")
		time.sleep(1)
	elif kondisi == "Biru":
		print("Sukses Servo Biru")
		print("DELAY MOTOR SERVO JALAN")
		time.sleep(1)
	elif kondisi == "Hijau":
		print("Sukses Servo Hijau")
		print("DELAY MOTOR SERVO JALAN")
		time.sleep(1)
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
		
		green_lower=np.array([25,52,72],np.uint8)
		green_upper=np.array([102, 255, 255],np.uint8)
	
		red= cv2.inRange(hsv, red_lower, red_upper)
		blue= cv2.inRange(hsv,blue_lower,blue_upper)
		yellow= cv2.inRange(hsv,yellow_lower,yellow_upper)
		green= cv2.inRange(hsv,green_lower,green_upper)
		
		cr= cv2.countNonZero(red)
		cb= cv2.countNonZero(blue)
		cy= cv2.countNonZero(yellow)
		cg= cv2.countNonZero(green)
		
		totalwarna=cb+cg+cr
		
		if totalwarna >= 1000:
			if i > 10 :
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
			break

if __name__ == "__main__":
	main()
