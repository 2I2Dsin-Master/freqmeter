T1 = 0
T0 = 0
T = 0
F = 0

# FREQUENCEMETRE v1.0 (c)Wp2022-04

def on_pulsed_p2_high():
    global T1
    T1 = pins.pulse_duration()
pins.on_pulsed(DigitalPin.P2, PulseValue.HIGH, on_pulsed_p2_high)

def on_pulsed_p2_low():
    global T0
    T0 = pins.pulse_duration()
pins.on_pulsed(DigitalPin.P2, PulseValue.LOW, on_pulsed_p2_low)

def on_forever():
    global T, F
    # basic.show_string("T1=")
    # basic.show_number(T1)
    # basic.show_string("T0=")
    # basic.show_number(T0)
    T = T0 + T1
    F = 1000000 / T
    basic.show_string("F=")
    basic.show_number(F)
    basic.pause(500)
basic.forever(on_forever)
