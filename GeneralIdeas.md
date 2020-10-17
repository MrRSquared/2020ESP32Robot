We have a few microcontrollers that could allow students to create cardboard robots on their devices...
    1) ESP32 
        This is an incredibly flexible board. Some noteable highlights...
            Wireless repl and file upload
            here is a link to the webrepl...
            http://micropython.org/webrepl
            Arduino capability for students wanting to learn CPP.
        Downsides...
            3.3v logic level means we need to use our own hbridge motor controllers.
                Also, it is possible that some devices will need level shifting as well.
            No accelerometer.
    2) Pyboard
        This is an incredibly flexible board. Some noteable highlights...
            Direct PWM control (May be able to conrol Vex MC directly)
            Onboard Accellerometer
            Flash memory may allow it to be programmed with a chromebook.
        Downsides
            No Wifi (not insurmountable)
            Need to research how to best control power
            