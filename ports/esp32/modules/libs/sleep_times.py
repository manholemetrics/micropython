import json
import time
from libs.config_dataclasses import StoredDeviceSleepTimes

sleep_times_json_loc: str = "store/configs/sleep_times.json"

sleep_times: StoredDeviceSleepTimes
with open(sleep_times_json_loc,'r' , encoding="utf8") as file:
    try:
        sleep_times_json = json.loads(file.read())
        sleep_times = StoredDeviceSleepTimes(**sleep_times_json)
    except:
        default_data = {
            "measurement_time": 0,
            "transmit_time": 10,
            "warning_level": False,
        }

        with open(sleep_times_json_loc,'w' , encoding="utf8")  as sleep_times_file:
            sleep_times_file.write(json.dumps(default_data))

        sleep_times = StoredDeviceSleepTimes(**default_data)


def process_warnings(warning: bool):
    """Setting times based on warning state"""
    from libs.configs import settings

    global sleep_times

    if warning:
        sleep_times.measurement_time = settings.warning_measurement_sleep_time_s
        if (
            sleep_times.transmit_time
            > int(time.time()) + settings.warning_message_sleep_time_s
        ):
            sleep_times.transmit_time = (
                int(time.time()) + settings.warning_message_sleep_time_s
            )
        sleep_times.warning_level = True
    else:
        sleep_times.measurement_time = settings.measurement_sleep_time_s
        sleep_times.warning_level = False

    with open(sleep_times_json_loc,"w",encoding='utf8') as sleep_times_file:
        sleep_times_file.write(sleep_times.toJSON())


def set_measurements_sleep_time():
    """Set the period of time to sleep for between measurements"""
    from libs.configs import settings

    global sleep_times

    sleep_times.measurement_time = settings.measurement_sleep_time_s
    with open(sleep_times_json_loc,"w",encoding='utf8') as sleep_times_file:
        sleep_times_file.write(sleep_times.toJSON())


def set_transmit_time():
    """Set the time at which to send next settings"""
    from libs.configs import settings

    global sleep_times

    sleep_times.transmit_time = int(
        settings.message_sleep_time_s + time.time())
    with open(sleep_times_json_loc,"w",encoding='utf8') as sleep_times_file:
        sleep_times_file.write(sleep_times.toJSON())
    print("saved sleep time")
