from typing import Tuple

class SGP30Reading:
    equivalent_co2: int
    total_voc: int

class SGP30:
    def __init__(self) -> None: ...
    def get_air_quality(self) -> SGP30Reading: ...
