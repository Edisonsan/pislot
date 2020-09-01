
import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#13: Counter In 27
#15: Counter Out 22
#7:  Door 04
#11: Power Set for Slot Machine. 11

_gpio_13 = 27
_gpio_15 = 22
_gpio_7 = 4
_gpio_11 = 17

GPIO.setup(_gpio_7, GPIO.IN)
GPIO.setup(_gpio_13, GPIO.IN)
GPIO.setup(_gpio_15, GPIO.IN)
GPIO.setup(_gpio_11, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

_gpio_counter_in = _gpio_13
_gpio_counter_out = _gpio_15
_gpio_door = _gpio_7
_gpio_power = _gpio_11

_door_open = False;
_door_prev_status = False;


GPIO.add_event_detect(_gpio_13, GPIO.FALLING)
GPIO.add_event_detect(_gpio_15, GPIO.FALLING)

try:
  while True:
#    if GPIO.input(_gpio_counter_in):
#      print('Counter In\n')

#    if GPIO.input(_gpio_counter_out):
#      print('Counter Out\n')

    if GPIO.event_detected(_gpio_13):
      print('Counter IN LOW\n')

    if GPIO.event_detected(_gpio_15):
      print('Counter OUT LOW\n')

    if(GPIO.input(5)):
        print('5')

    if(GPIO.input(6)):
        print('6')

    if(GPIO.input(13)):
        print('13')

    if(GPIO.input(19)):
        print('19')

    if(GPIO.input(26)):
        print('26')

    if(GPIO.input(18)):
        print('18')

    if(GPIO.input(23)):
        print('23')

    if(GPIO.input(24)):
        print('24')

    if(GPIO.input(25)):
        print('25')

    if(GPIO.input(12)):
        print('12')

    if(GPIO.input(16)):
        print('16')

    if(GPIO.input(20)):
        print('20')

    if(GPIO.input(21)):
        print('21')

    if GPIO.input(_gpio_door):
      if not _door_open:
	_door_open = True
    	_door_prev_status = False;

      if(_door_open):
        GPIO.output(_gpio_power, GPIO.HIGH)
        if not _door_prev_status:
          print('Door Closed')
          print('Slot Machine Power Supply ON')

      _door_prev_status = True
    else:
      GPIO.output(_gpio_power, GPIO.LOW)
      if(_door_open):
        print('Door Open')

        print('Slot Machine OFF')
      _door_open = False

    sleep(0.1)
finally:
  GPIO.cleanup()


