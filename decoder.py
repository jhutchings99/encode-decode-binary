from machine import Pin
import time

clock = Pin(15, Pin.IN, Pin.PULL_DOWN)
data = Pin(14, Pin.IN, Pin.PULL_DOWN)

bits = ""
message = ""

def binary_to_char(bin_str):
    return chr(int(bin_str, 2))

last_signal_time = time.ticks_ms()

while True:
    # rising edge
    while not clock.value():
        if time.ticks_ms() - last_signal_time > 2000 and message:
            print(message)
            message = ""

    # falling edge
    while clock.value():
        pass

    last_signal_time = time.ticks_ms()

    # read data after falling edge
    time.sleep_ms(1)
    bit = data.value()
    bits += str(bit)

    if len(bits) == 8:        
        char = binary_to_char(bits)
        message += char
        bits = ""
