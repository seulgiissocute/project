import RPi.GPIO as GPIO

import time
import spidev
import telepot

telegram_id = '1417051484'
my_token = '1430018325:AAFJT1QvjzRoc-jM3xYbaAX-RTq10-qPjN4'

bot = telepot.Bot(my_token)

msg = '수분 부족! 화분에 물을 공급합니다.'
msg2 = '수분 공급이 완료되었습니다.'

a = 1
b = 1

A1A = 5

A1B = 6

HUM_THRESHOLD=33

HUM_MAX=0



GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(A1A, GPIO.OUT)

GPIO.output(A1A, GPIO.LOW)

GPIO.setup(A1B, GPIO.OUT)

GPIO.output(A1B, GPIO.LOW)
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000

def read_spi_adc(adcChannel):
    adcValue=0

    buff =spi.xfer2([1,(8+adcChannel)<<4,0])

    adcValue = ((buff[1]&3)<<8)+buff[2]

    return adcValue


def map(value,min_adc, max_adc, min_hum,max_hum) :
    
    adc_range=max_adc-min_adc

    hum_range=max_hum-min_hum

    scale_factor=float(adc_range)/float(hum_range)

    return min_hum+((value-min_adc)/scale_factor)

try:
    adcChannel=0

    while True :
        adcValue=read_spi_adc(adcChannel)

        hum=100-int(map(adcValue,HUM_MAX,1023,0,100))

        if hum <= HUM_THRESHOLD :
            
            print(hum)
            
            if a == 1:
                bot.sendMessage(chat_id = telegram_id, text = msg)
                a -= 1
            
            GPIO.output(A1A,GPIO.HIGH) 

            GPIO.output(A1B,GPIO.LOW)

        else :
            
            print(hum)
            
            if b == 1:
                bot.sendMessage(chat_id = telegram_id, text = msg2)
                b -= 1

            GPIO.output(A1A,GPIO.LOW)

            GPIO.output(A1B,GPIO.LOW)

        time.sleep(0.5)
finally:
    GPIO.cleanup()
    spi.close()
