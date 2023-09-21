'''Controller for using the maxbotics sensor'''

from machine import ADC, Pin, UART
from time import sleep_ms, time
sensor = ADC(Pin(35))
# _sensor separate pin which decides what we get (filtered analogue or unflitered analogue. PIN 4 High gives unfiltered analogue data)
# _sensor.atten(ADC.ATTN_11DB)
# 12
PIN_HIGH_VALUE = 1
# io 27 for load switch 18 for unfiltered or filtered
_load_switch = Pin(27, Pin.OUT) 
uart = UART(1,9600)

###########################
# 7092 verion, no analogue uses inverted serial
uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=32, rx=4, invert=UART.INV_RX)
###########################
# 7389 with analogue, non inverted serial. io uart (real time range data ->) 
# uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=32, rx=4)
###########################

sensor.atten(ADC.ATTN_11DB)

def get_reading_mm() -> int:
    '''Return the sensor reading converted to mm'''
    for _ in range(10):
        try:
            data = uart.read()
            data = data.decode('ascii').split('R')
            if len(data) > 1:
                measurement = data[1][:-1]
                print(measurement)
                measurement = int(measurement)*10
                return measurement
        except:
            ...
        sleep_ms(200)
    return 0
    #raise Exception

analogue_data_list_length = 1024
analogue_data_list: list[int] = [0] * analogue_data_list_length

def get_analogue(period = 0.5):
    if not is_sensor_on():
        print("Sensor was off for getting analogue data, turning it on now")
        turn_on_sensor()

    start_time = time()
    idx = 0
    
    # collect as many samples as possible
    while time() - start_time < period and idx < analogue_data_list_length:
        analogue_data_list[idx] = sensor.read()
        idx += 1
        
    # clear obsolete values
    while idx < analogue_data_list_length:
        analogue_data_list[idx] = 0
        idx += 1
    
    return analogue_data_list

def get_reading_raw() -> int:
    '''Return the raw value from the sensor'''
    return get_reading_mm()

def is_sensor_on() -> int:
    result = _load_switch.value() == PIN_HIGH_VALUE
    return result
    

def turn_off_sensor() -> None:
    print('turning off sensor')
    # turn the load switch off
    _load_switch.value(0)

def turn_on_sensor() -> None:
    print('turning on sensor')
    _load_switch.value(1)
