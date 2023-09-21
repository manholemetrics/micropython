import json

from libs.config_dataclasses import StoredDeviceSettings, StoredDeviceSecrets
from messages.device_settings_upb2 import DeviceSettings

settings_json_loc: str = "store/configs/settings.json"
def open_settings_json(mode: str):
    return open(settings_json_loc, mode, encoding="utf8")

secrets_json_loc: str = "store/configs/secrets.json"
def open_secrets_json(mode: str):
    return open(secrets_json_loc, mode, encoding="utf8")

settings: StoredDeviceSettings
with open_settings_json('r') as file:
    settings_dict = json.loads(file.read())
    settings = StoredDeviceSettings(**settings_dict)

secrets: StoredDeviceSecrets
with open_secrets_json('r') as file:
    secrets_json = json.loads(file.read())
    secrets = StoredDeviceSecrets(**secrets_json)

def save_settings():
    '''Save the current settings'''
    global settings
    with open_settings_json('w') as file:
        file.write(settings.toJSON())

def save_new_settings(new_settings: DeviceSettings):
    '''Store the settings taken from the server, ignoring the code version'''
    global settings
    with open_settings_json('w') as file:
        settings.measurement_sleep_time_s = new_settings.measurement_interval_s
        settings.message_sleep_time_s = new_settings.message_interval_s
        settings.warning_measurement_sleep_time_s = new_settings.warning_measurement_interval_s
        settings.warning_message_sleep_time_s = new_settings.warning_message_interval_s
        settings.warning_distance_mm = new_settings.warning_distance_mm
        # don't write code version
        file.write(settings.toJSON())

def save_code_version(code_version : int):
    '''Store a new code version'''
    global settings

    with open_settings_json('w') as file:
        settings.code_version = code_version
        file.write(settings.toJSON())
