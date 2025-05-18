# Embedded Voltmeter - Raspberry Pi Pico (MicroPython)

*Graduation project from DECI L3 Semester 2*

A MicroPython project simulating a voltmeter using Raspberry Pi Pico on Wokwi. The system reads analog inputs from a slide potentiometer, photoresistor (LDR), and temperature sensor (NTC), and displays voltage values on a 4-digit 7-segment display. Pushbutton interrupts with debouncing trigger measurements.

---

## Project Overview

Embedded Voltmeter project using MicroPython on Raspberry Pi Pico with Wokwi simulation. Reads analog voltage values from an external device connected by the user to the ADC pin, and displays the voltage on a 4-digit 7-segment display. Includes pushbutton control with interrupt handling and debouncing.

### Key Features

- Reads analog voltage from a slide potentiometer, LDR, and NTC sensors via ADC on GPIO 26.
- Displays voltage readings on a multiplexed 4-digit 7-segment display with minimal flicker.
- Uses a pushbutton with an interrupt handler for triggering measurements, including 200ms debounce.
- Organized breadboard placement for neat wiring and component layout.
- Supports ADC value reading with accurate voltage scaling between 0.000V and 3.300V.

---

## Components Used

- Raspberry Pi Pico microcontroller
- 4-digit 7-segment display (multiplexed)
- Pushbutton (GPIO16) with interrupt and debouncing
- Slide potentiometer (analog input via GPIO26 ADC)
- Photoresistor (LDR) sensor
- Analog temperature sensor (NTC)
- Breadboard for component placement and wiring

---

## How to Run

1. Open the project in the [Wokwi Simulator](https://wokwi.com/).  
2. Load the `diagram.js` to see the circuit schematic.  
3. Upload and run the `main.py` MicroPython script on the Raspberry Pi Pico.  
4. Adjust the slide potentiometer or interact with the LDR and NTC sensors in the simulation.  
5. Press the pushbutton to trigger voltage measurements, which will be displayed on the 7-segment display.  
6. Observe the voltage readings corresponding to your adjustments, displayed clearly and with minimal flicker.
7. You could run directly from the link below.

---

## My Role

I designed and implemented the full MicroPython code to read analog sensor values accurately using ADC, handled interrupts and debouncing for pushbutton input, and controlled the multiplexed 7-segment display for stable voltage readouts. I ensured compliance with the project requirements and correct circuit implementation on Wokwi.

---

## Project Links

- [Wokwi Project Link](https://wokwi.com/projects/431299110050596865)  
- [GitHub Repository](https://github.com/Begadbigo/embedded-voltmeter)
