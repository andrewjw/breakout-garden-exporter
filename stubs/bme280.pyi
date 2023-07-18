from typing import Any

class BME280:
    def __init__(self, i2c_dev: Any) -> None: ...
    def setup(self) -> None: ...
    def get_temperature(self) -> float: ...
    def get_pressure(self) -> float: ...
    def get_humidity(self) -> float: ...