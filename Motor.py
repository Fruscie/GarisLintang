import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

MKiri1 = 19
MKiri2 = 26
MKanan1 = 27
MKanan2 = 17

GPIO.setup(MKiri1, GPIO.OUT)
GPIO.setup(MKiri2, GPIO.OUT)
GPIO.setup(MKanan1, GPIO.OUT)
GPIO.setup(MKanan2, GPIO.OUT)


try:
  while True:
    print('Maju')
    p1=GPIO.PWM(MKiri1,100)
    p2=GPIO.PWM(MKiri2, 100)
    p3=GPIO.PWM(MKanan1,100)
    p4=GPIO.PWM(MKanan2, 100)
    p2.start(30)
    p3.start(30)
    time.sleep(0.8)
    p2.start(0)
    p3.start(0)
    p2.start(30)
    p4.start(30)
    time.sleep(0.8)
    #p1.start(40)#maju
    #p2.start(100)
    #p1.start(28)#mundur
    #p2.start(100)
    #p1.start(30)#kiri
    #p2.start(100)
    #time.sleep(0.6)
    #p1.start(70)#kanan
    #p2.start(60)
    #time.sleep(0.6)
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    break
except KeyboardInterrupt:
  p1.stop()
  p2.stop()
  GPIO.cleanup()
