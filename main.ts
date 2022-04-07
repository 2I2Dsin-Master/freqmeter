let T1 = 0
let T0 = 0
let T = 0
let F = 0
//  FREQUENCEMETRE v1.0 (c)Wp2022-04
pins.onPulsed(DigitalPin.P2, PulseValue.High, function on_pulsed_p2_high() {
    
    T1 = pins.pulseDuration()
})
pins.onPulsed(DigitalPin.P2, PulseValue.Low, function on_pulsed_p2_low() {
    
    T0 = pins.pulseDuration()
})
basic.forever(function on_forever() {
    
    //  basic.show_string("T1=")
    //  basic.show_number(T1)
    //  basic.show_string("T0=")
    //  basic.show_number(T0)
    T = T0 + T1
    F = 1000000 / T
    basic.showString("F=")
    basic.showNumber(F)
    basic.pause(500)
})
