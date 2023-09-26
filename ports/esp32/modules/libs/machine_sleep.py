from machine import (
    reset_cause,
    deepsleep as sleep,
    PWRON_RESET,
    HARD_RESET,
    WDT_RESET,
    DEEPSLEEP_RESET,
    SOFT_RESET,
)


def deepsleep(time_s: int):
    print("sleeping for", time_s)
    sleep(time_s * 1000)


def get_reset_cause():
    cause = reset_cause()
    print(cause)
    if cause == PWRON_RESET:
        print("[rst] Device powered on")
        return "INCOMPLETE"
    elif cause == HARD_RESET:
        print("[rst] Device reset due to hardware reset")
    elif cause == WDT_RESET:
        print("[rst] Device reset due to watchdog")
    elif cause == DEEPSLEEP_RESET:
        print("[rst] Device woke up from deep sleep (including short sleep)")
    elif cause == SOFT_RESET:
        print("[rst] Software reset")
    else:
        print("[rst] Unknown reset cause")
