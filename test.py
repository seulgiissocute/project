import RPi.GPIO as GPIO

import time
import spidev
import telepot

telegram_id = '1417051484'
my_token = '1430018325:AAFJT1QvjzRoc-jM3xYbaAX-RTq10-qPjN4'

bot = telepot.Bot(my_token)

msg = '수분 부족! 화분에 물을 공급합니다.'
msg2 = '수분 공급이 완료되었습니다.'

#While문에서 텔레그램 문자 한번 보내기위한 초기값
temp = 1
cnt = 1
cnt2 = 1

#Moter Drive 연결 PIN
A1A = 5
A1B = 6

# 습도 임계치(%)
HUM_THRESHOLD = 33

#센서를 물에 담갔을때의 토양습도센서 출력 값(백분율)
HUM_MAX = 0

#모터 드라이버 초기 설정

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(A1A, GPIO.OUT)
GPIO.output(A1A, GPIO.LOW)
GPIO.setup(A1B, GPIO.OUT)
GPIO.output(A1B, GPIO.LOW)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000

#LED설정 및 실행
def led_on(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)

#LED설정 및 종료
def led_off(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.cleanup(pin)

 #ADC 값을 가져오는 함수
def read_spi_adc(adcChannel):
    adcValue = 0
    buff = spi.xfer2([1, (8 + adcChannel) << 4, 0])
    adcValue = ((buff[1] & 3) << 8) + buff[2]
    return adcValue

# 센서 값을 백분율로 변환하기위한 map 함수
def map(value, min_adc, max_adc, min_hum, max_hum):
    adc_range = max_adc - min_adc
    hum_range = max_hum - min_hum
    scale_factor = float(adc_range) / float(hum_range)
    return min_hum + ((value - min_adc) / scale_factor)


#메인
try:
    adcChannel = 0
    while True:
        adcValue = read_spi_adc(adcChannel)

        # 가져온 데이터를 %단위로 변환.
        hum = 100 - int(map(adcValue, HUM_MAX, 1023, 0, 100))

        # 임계치보다 수분값이 작으면 실행
        if hum <= HUM_THRESHOLD:

            print(hum)

            led_on(17)

            #텔레그램에서 문자를 한번 보내기 위한 if문
            if temp != 0:
                cnt = 0
                temp = 0

            if cnt == 0:
                bot.sendMessage(chat_id=telegram_id, text=msg)
                cnt += 1

            # 워터펌프 가동
            GPIO.output(A1A, GPIO.HIGH)
            GPIO.output(A1B, GPIO.LOW)

        else:

            print(hum)

            led_off(17)

            # 텔레그램에서 문자를 한번 보내기 위한 if문
            if temp != 1:
                cnt2 = 0
                temp=1

            if cnt2 == 0:
                bot.sendMessage(chat_id=telegram_id, text=msg2)
                cnt2 -= 1

            GPIO.output(A1A, GPIO.LOW)
            GPIO.output(A1B, GPIO.LOW)

        time.sleep(0.5)
finally:
    GPIO.cleanup()
    spi.close()
