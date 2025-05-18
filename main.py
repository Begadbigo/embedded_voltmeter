# imports
import machine
import math
import time
from machine import Pin
from time import sleep


time.sleep(0.1)

#######################################
# Pin and constant definitions
#######################################
ADC_INPUT = machine.ADC(26)
BUTTON =  Pin(16, Pin.IN, Pin.PULL_UP)
SEVEN_SEGMENT_START_PIN = 0
DISPLAY_COUNT = 4
DECIMAL_PRECISION = 3
button_pressed = False


# HEX values for 7 segment display values
digit_list_hex = [
    0x40,  # 0
    0x79,  # 1
    0x24,  # 2
    0x30,  # 3
    0x19,  # 4
    0x12,  # 5
    0x02,  # 6
    0x78,  # 7
    0x00,  # 8
    0x10,  # 9
    0x08,  # A
    0x03,  # B
    0x46,  # C
    0x21,  # D
    0x06,  # E
    0x0E,  # F
    0x7F   # Empty
]

#######################################
# Global variables
#######################################
display_value = 0
segment_pins = []
display_select_pins = []
current_display_index = DISPLAY_COUNT -1  # to keep track of which digit is currently being displayed
display_timer = None
counter_timer = None

#######################################
# Function definitions
#######################################

# Function to disable timer that triggers scanning 7 segment displays
def disable_display_timer():
    global display_timer
    display_timer.deinit()

# Function to enable timer that triggers scanning 7 segment displays
def enable_display_timer():
    global display_timer
    display_timer.init(period=30, mode=machine.Timer.PERIODIC, callback=scan_display)

# Function to handle scanning 7 segment displays
# Display the value stored in the display_value global variable
# on available 7-segment displays
def scan_display(timer_int):
    global current_display_index, display_value

    # Extract the digit corresponding to the current display index
    digit = int((display_value // math.pow(10, current_display_index))) % 10

    # Display the digit,
    # enable the decimal point if the current digit index equals to the set decimal precision
    display_digit(digit, current_display_index, 
        current_display_index == DECIMAL_PRECISION and 0 != DECIMAL_PRECISION)

    # Move to the next display
    current_display_index = (current_display_index - 1)
    if current_display_index < 0:
        current_display_index = DISPLAY_COUNT -1

# Function display the given value on the display with the specified index
# dp_enable specifies if the decimal pooint should be on or off
def display_digit(digit_value, digit_index, dp_enable=False):
    # Ensure the value is valid
    if digit_value < 0 or digit_value > len(digit_list_hex):
        return

    # Deselect all display select pins
    for pin in display_select_pins:
        pin.value(0)

    # Set the segments according to the digit value
    mask = digit_list_hex[digit_value]
    for i in range(7):  # 7 segments from A to G
        segment_pins[i].value((mask >> i) & 1)

    # Set the DP if it's enabled
    segment_pins[7].value(1 if dp_enable == False else 0)

    # If digit_index is -1, activate all display select pins
    if digit_index == -1:
        for pin in display_select_pins:
            pin.value(1)
    # Otherwise, ensure the index is valid and activate the relevant display select pin
    elif 0 <= digit_index < DISPLAY_COUNT:
        display_select_pins[digit_index].value(1)

# Function to test avaiable 7-segment displays
def display_value_test():
    for i in range(16):
        display_digit(i, 0)
        time.sleep(0.5)


#functioon for button handler
def int_handler(pin):
    global button_pressed
    button_pressed = True

BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=int_handler)

# Function to setup GPIO/ADC pins, timers and interrupts
def setup():
    global segment_pins, display_select_pins
    global display_timer, counter_timer

    # Set up display select pins
    for i in range(SEVEN_SEGMENT_START_PIN + 8, SEVEN_SEGMENT_START_PIN + 8 + DISPLAY_COUNT):
        pin = machine.Pin(i, machine.Pin.OUT)
        pin.value(0)
        display_select_pins.append(pin)

    # Set up seven segment pins
    for i in range(SEVEN_SEGMENT_START_PIN, SEVEN_SEGMENT_START_PIN + 8):
        pin = machine.Pin(i, machine.Pin.OUT)
        pin.value(1)
        segment_pins.append(pin)

    # Start the timer interrupt for scanning
    display_timer = machine.Timer()
    enable_display_timer()


current_state = 0
previous_state = 1

if __name__ == '__main__':
    setup()
    while True:
        voltage = (ADC_INPUT.read_u16())*(3.3/((2**16)-1))

        
        if button_pressed is True:
            button_pressed = False

            if previous_state != current_state:
                current_state = 1
                # Read ADC digital output
                voltage = (ADC_INPUT.read_u16())*(3.3/((2**16)-1))
                display_value = voltage *1000
                print("voltage:",voltage)
                sleep(0.1)

            else:
                current_state = 0
                sleep(0.1)
        sleep(0.1)