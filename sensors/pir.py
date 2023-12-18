import RPi.GPIO as GPIO


class PIR:
    def __int__(self, pin, name):
        self.pin = pin
        self.name = name


def run_pir_loop(pir, motion_detected, stop_event, publish_event, settings):
    GPIO.setup(pir.pin, GPIO.IN)
    GPIO.add_event_detect(pir.pin, GPIO.RISING, callback=lambda channel: motion_detected(publish_event, settings))
    while True:
        if stop_event.is_set():
            GPIO.remove_event_detect(pir.pin)
            break
