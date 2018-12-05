import RPi.GPIO as GPIO
import time
import faceSet
import face_training
import face_recognition
import cctv

GPIO.setmode(GPIO.BCM)

sensor = 23
Sled = 20
Fled = 21

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(Sled, GPIO.OUT)
GPIO.setup(Fled, GPIO.OUT)

print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"

while True:
    if GPIO.input(sensor):
        print "Motion Detected"
        faceSet.dataset()
        face_training.train()
        face_recognition.recognition()
        if face_recognition.recognition() == 100:
            GPIO.output(Sled, True)
            time.sleep(2)

        else :
            GPIO.output(Fled, False)
            Camera_cctv()
            time.sleep(2)




GPIO.cleanup()
