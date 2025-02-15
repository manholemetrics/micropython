import machine

def sleep_callback(timer):
    # disable interrupts
    machine.disable_irq()
    print('timer called')
    try:
        from logic.utils.sleep import standard_sleep
        standard_sleep()
    finally:
        machine.enable_irq()

def setup_turn_off_timer():
    print('start2')
    timer = machine.Timer(0)
    print('start3')
    timer.init(period=2100000, mode=machine.Timer.ONE_SHOT, callback=sleep_callback)
    return timer

def start_timer():
    setup_turn_off_timer()
    