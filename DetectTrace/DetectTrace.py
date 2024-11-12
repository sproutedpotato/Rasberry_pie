import RPi.GPIO as GPIO
import time
from time import sleep
import datetime
import subprocess

TRIG_PIN = 20
ECHO_PIN = 21
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
BUZZER_PIN = 22
def initPizeo(): # 피에조 부저 초기화
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BUZZER_PIN, GPIO.OUT)

def Pizeo_On():
	GPIO.output(BUZZER_PIN, GPIO.HIGH)

def Pizeo_Off():
	GPIO.output(BIZZER_PIN, GPIO.LOW)

def initUltrasonic(): # 초음파 센서 초기화
	GPIO.setup(TRIG_PIN, GPIO.OUT)
	GPIO.setup(ECHO_PIN, GPIO.IN)

def controlUltrasonic(): # 초음파 센서 제어 / 거리 측정 후 반환
	distance = 0.0
	GPIO.output(TRIG_PIN, False)
	time.sleep(0.5)
	GPIO.output(TRIG_PIN, True)
	time.sleep(0.00001)
	GPIO.output(TRIG_PIN, False)
	while GPIO.input(ECHO_PIN) == 0:
		pulse_start = time.time()
	while GPIO.input(ECHO_PIN) == 1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17000
	distance = round(distance, 2)
	return distance

GPIO.setmode(GPIO.BCM) # GPIO 모드 설정
distance = 0.0 
index_jpg = 0
index_vid = 0 # 거리변수, index_jpg, index_vid변수 선언
initUltrasonic() # 초음파 센서 초기화
print("Ultrasonic Operating...")
try: # 프로그램 실행
	while True:
		distance = controlUltrasonic() # 거리 측정
		if distance < n: # 일정 거리 이상 들어오면
			current = datetime.datetime.now()
			print("Someone's on the Approch : ", current) # 들어온 시간 출력
			try:
				while True:
					if GPIO.input(18) == True: # 움직임 감지시
						print("Detect time : ", current) # 감지된 시간 출력
						take_pic = f'libcamera-jpeg -o temp_{index_jpg}.jpg'
						pic_time = time.time()
						process_camera = subprocess.Popen(take_pic, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # 셸에서 사진 촬영
						output_c, error_c = process_camera.communicate()
						if output_c:
							print("Command output : ", output.decode()) # 촬영 명령이 수행되었다고 출력
						if error_c:
							print("Error : ", error.decode()) # 촬영되지 않았을 시 에러메시지 출력
							break
						index_jpg += 1

						if ((GPIO.input(18) == True and distance < n) and (time.time() - pic_time) > 5): # 5초 후에도 움직임이 감지되고, 일정 거리 내에 있는지?
							while (GPIO.input(18) == True and distance < n):
								Piezo_On()
								take_vid = f'libcamera -o vid_t1_{index_vid}.h264 -t 60000'
								process_video = subprocess.Popen(take_pic, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # 셸에서 비디오 촬영
								output_v, error_v = process.communicate()
								if output_v:
									print("Command output : ", output.decode()) # 촬영 명령이 수행되었다고 출력
								if error_v:
									print("Error : ", output.decode()) # 촬영되지 않았을 시 에러메시지 출력
								index_vid += 1
						else:
							Pizeo_Off()
							break

					if GPIO.output(18) == False: # 감지되지 않으면
						break # 원래대로 돌아감


except KeyboardInterrupt:
	GPIO.cleanup()