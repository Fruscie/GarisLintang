import RPi.GPIO as GPIO
import time

servoPIN1 = 21
servoPIN2 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
AwalAngkat = 50
AwalCapit = 100

p1 = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
p1.start(0) # Initialization
p2 = GPIO.PWM(servoPIN2, 50) # GPIO 17 for PWM with 50Hz
p2.start(0) # Initialization
def Capit(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPIN1, True)
	p1.ChangeDutyCycle(duty)
	time.sleep(2)
##	p1.start(0)   
	GPIO.output(servoPIN1, False)
	#p1.start(0) 


def Angkat(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPIN2, True)
	p2.ChangeDutyCycle(duty)
	time.sleep(2)
	p2.start(0)
	GPIO.output(servoPIN2, False)

	
def AwalServo():
    Capit(AwalCapit)
    Angkat(AwalAngkat)
         
try:
  while True:
      Capit(70)
##    AwalServo()
##    print('buka')
      
    
      Angkat(50)
      Capit(100)
      Angkat(110)
      time.sleep(0.5)
      Angkat(90)
      Capit(70)
      Capit(100)
#     
##    print('tutup')
##    Capit(100)
##    print('naik')
##    Angkat(100)
##    time.sleep(1)
##    Angkat(AwalAngkat)
##    print('buka')
##    Capit(0)
##    AwalServo()
#       p1.start(0)
      break
except KeyboardInterrupt:
  p1.stop()
  p2.stop()
  GPIO.cleanup()
  
