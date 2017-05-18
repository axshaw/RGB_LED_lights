# ch02_04.py file

import wiringpi
import time

# initialize
wiringpi.wiringPiSetup()  # WiPi mode

# define shift reg pins
DATA = 6
LATCH = 5
CLK = 4

OUTPUT = 1
LOW = 0
HIGH = 1

# common anode digital tube 16 BCD code
LED_BCD = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]

wiringpi.pinMode(DATA, OUTPUT)
wiringpi.pinMode(LATCH, OUTPUT)
wiringpi.pinMode(CLK, OUTPUT)

# initialization
print("Initialization...")
wiringpi.digitalWrite(LATCH, LOW)
wiringpi.digitalWrite(CLK, LOW)


def LED_display(LED_number, LED_display, LED_dp):
    hc_ledcode_temp = 0

    if LED_display > 15:
        LED_display = 0

    hc_ledcode = LED_BCD[LED_display]
    for i in range(0, 8):
        hc_ledcode_temp <<= 1
        if hc_ledcode & 0x01:
            hc_ledcode_temp |= 0x01

        hc_ledcode >>= 1

    if LED_dp:
        hc_ledcode_temp &= 0xfe

    hc_disp = hc_ledcode_temp
    if LED_number == 0:
        hc_disp |= 0x8000
    elif LED_number == 1:
        hc_disp |= 0x4000
    elif LED_number == 2:
        hc_disp |= 0x2000
    elif LED_number == 3:
        hc_disp |= 0x1000

    write_74HC595_ShiftOUTPUT(hc_disp)


def write_74HC595_ShiftOUTPUT(data_a):

    wiringpi.digitalWrite(LATCH, LOW)
    wiringpi.digitalWrite(CLK, LOW)

    for i in range(0, 16):
        if data_a & 0x0001:
            wiringpi.digitalWrite(DATA, HIGH)
        else:
            wiringpi.digitalWrite(DATA, LOW)

        wiringpi.digitalWrite(CLK, HIGH)
        wiringpi.digitalWrite(CLK, LOW)
        data_a >>= 1

    wiringpi.digitalWrite(LATCH, HIGH)


print("Running...")
try:
    timer = 0
    digit = 0
    while 1:
        LED_display(0, digit, 0)
        time.sleep(0.01)
        LED_display(1, digit, 0)
        time.sleep(0.01)
        LED_display(2, digit, 0)
        time.sleep(0.01)
        LED_display(3, digit, 0)
        time.sleep(0.01)

        timer += 1
        if timer > 10:
            time.sleep(0.05)
            timer = 0
            digit += 1
            if digit > 9:
                digit = 0

except KeyboardInterrupt:
    write_74HC595_ShiftOUTPUT(0)

print("done")
