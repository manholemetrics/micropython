import json


class StoredDeviceSettings:
    def set_default_times(self: "StoredDeviceSettings"):
        self.message_sleep_time_s = 60 * 60 * 12
        self.measurement_sleep_time_s = 60 * 15
        self.warning_message_sleep_time_s = 60 * 60 * 12
        self.warning_measurement_sleep_time_s = 60 * 15

    def toJSON(self: "StoredDeviceSettings"):
        return json.dumps(
            {
                "analogue_resource": self.analogue_resource,
                "code_version": self.code_version,
                "connection_resource": self.connection_resource,
                "measurement_resource": self.measurement_resource,
                "measurement_sleep_time_s": self.measurement_sleep_time_s,
                "message_sleep_time_s": self.message_sleep_time_s,
                "send_analogue": self.send_analogue,
                "server_url": self.server_url,
                "setup_complete": self.setup_complete,
                "setup_resource": self.setup_resource,
                "server_host": self.server_host,
                "update_resource": self.update_resource,
                "warning_distance_mm": self.warning_distance_mm,
                "warning_measurement_sleep_time_s": self.warning_measurement_sleep_time_s,
                "warning_message_sleep_time_s": self.warning_message_sleep_time_s,
                "max_measurements": self.max_measurements
            }
        )

    def __init__(
        self: "StoredDeviceSettings",
        analogue_resource: str = "/analogue",
        code_version: int = 0,
        connection_resource: str = "/connection",
        measurement_resource: str = "/data_resource",
        measurement_sleep_time_s: int = 5,
        message_sleep_time_s: int = 31,
        send_analogue: int = 0,
        server_url: str = '"host.docker.internal:8003"',
        server_host: str = "0.0.0.0",
        setup_complete: str = "INCOMPLETE",
        setup_resource: str = "/setup_resource",
        update_resource: str = "/update_json",
        warning_distance_mm: int = 1400,
        warning_measurement_sleep_time_s: int = 2,
        warning_message_sleep_time_s: int = 10,
        max_measurements: int = 600,
    ):
        self.analogue_resource = analogue_resource
        self.code_version = code_version
        self.connection_resource = connection_resource
        self.measurement_resource = measurement_resource
        self.measurement_sleep_time_s = measurement_sleep_time_s
        self.message_sleep_time_s = message_sleep_time_s
        self.send_analogue = send_analogue
        self.server_url = server_url
        self.server_host = server_host
        self.setup_complete = setup_complete
        self.setup_resource = setup_resource
        self.update_resource = update_resource
        self.warning_distance_mm = warning_distance_mm
        self.warning_measurement_sleep_time_s = warning_measurement_sleep_time_s
        self.warning_message_sleep_time_s = warning_message_sleep_time_s
        self.max_measurements = max_measurements


class StoredDeviceSleepTimes:
    def toJSON(self: "StoredDeviceSleepTimes"):
        return json.dumps(
            {
                "measurement_time": self.measurement_time,
                "transmit_time": self.transmit_time,
                "warning_level": self.warning_level,
            }
        )

    def __init__(
        self: "StoredDeviceSleepTimes",
        measurement_time: int = 2,
        transmit_time: int = 10,
        warning_level: bool = True,
    ):
        self.measurement_time = measurement_time
        self.transmit_time = transmit_time
        self.warning_level = warning_level


class StoredDeviceSecrets:
    def toJSON(self: "StoredDeviceSecrets"):
        return json.dumps(
            {
                "analogue": self.analogue,
                "device_id": self.device_id,
                "device_secret": self.device_secret,
                "encryption_key": self.encryption_key,
            }
        )

    def __init__(
        self: "StoredDeviceSecrets",
        analogue: bool = True,
        device_id: int = 213875875,
        device_secret: int = 1909419,
        encryption_key: str = "DEFAULT_ENCRYPT_KEY",
    ):
        self.analogue = analogue
        self.device_id = device_id
        self.device_secret = device_secret
        self.encryption_key = encryption_key


class StoredSetupMessage:
    def toJSON(self: "StoredSetupMessage"):
        return json.dumps(
            {
                "coordinates": self.coordinates,
                "company_id": self.company_id,
                "account_id": self.account_id,
                "max_distance_mm": self.max_distance_mm,
                "setup_notes": self.setup_notes,
                "manhole_thickness_mm": self.manhole_thickness_mm,
            }
        )

    def __init__(
        self: "StoredSetupMessage",
        coordinates: tuple[float, float] = (0, 0),
        company_id: str = "company",
        account_id: str = "account_id",
        max_distance_mm: int = 0,
        setup_notes: str = "notes",
        manhole_thickness_mm: int = 0,
    ):
        self.coordinates = coordinates
        self.company_id = company_id
        self.account_id = account_id
        self.max_distance_mm = max_distance_mm
        self.setup_notes = setup_notes
        self.manhole_thickness_mm = manhole_thickness_mm
