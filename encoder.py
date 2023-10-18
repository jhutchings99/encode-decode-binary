from machine import Pin
import time

clock = Pin(15, Pin.OUT)
send = Pin(14, Pin.OUT)

PULSE_WIDTH = 2
MESSAGE = "hello world! WOOO"

def char_to_binary(char):
    bits = bin(ord(char))[2:]
    while len(bits) < 8:
        bits = "0" + bits
    return bits

# convert message to list of bits
bits = []
for char in MESSAGE:
    char_bits = char_to_binary(char)
    for char_bit in char_bits:
        bits.append(int(char_bit))
        
while bits:
    # rising edge 
    clock.value(1)
    st = time.ticks_ms()
    while time.ticks_ms() - st < PULSE_WIDTH:
        pass

    # falling edge
    clock.value(0)
    st = time.ticks_ms()
    while time.ticks_ms() - st < PULSE_WIDTH / 2: # wait for half of the falling edge
        pass

    send.value(bits.pop(0))

    st = time.ticks_ms()
    while time.ticks_ms() - st < PULSE_WIDTH / 2: # wait for other half
        pass
