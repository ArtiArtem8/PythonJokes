from dataclasses import dataclass

from geopy.distance import distance

UNIT_METHODS = {
    'km',
    'm'
}


@dataclass(frozen=True)
class Location:
    """Location for order"""
    latitude: float
    longitude: float

    def distance_to(self, other: 'Location', unit: str = 'km') -> float:
        """Calculate the distance to another location."""
        if not isinstance(other, Location):
            raise TypeError("The 'other' parameter must be an instance of 'Location'.")
        if unit not in UNIT_METHODS:
            raise ValueError(f"Invalid unit. Use {', '.join(map(repr, UNIT_METHODS))}.")
        return getattr(distance((self.latitude, self.longitude),
                                (other.latitude, other.longitude)), unit)

    def is_nearby(self, other: 'Location', threshold: float, unit: str = 'km') -> bool:
        """Check if another location is nearby within a threshold distance."""
        if not isinstance(other, Location):
            raise TypeError("The 'other' parameter must be an instance of 'Location'.")
        if threshold <= 0:
            raise ValueError("Threshold must be a positive number.")
        if unit not in UNIT_METHODS:
            raise ValueError(f"Invalid unit. Use {', '.join(map(repr, UNIT_METHODS))}.")
        _distance = self.distance_to(other, unit)
        return _distance <= threshold


if __name__ == '__main__':
    location1 = Location(-41.32, 174.81)
    location2 = Location(-40.96, 170.50)
    print(f"{location1=} {location2=}")
    print("Distance:", location1.distance_to(location2), "km")
    print("Nearby:", location1.is_nearby(location2, 500), "km")
