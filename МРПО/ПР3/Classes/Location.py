from dataclasses import dataclass

from geopy.distance import distance


@dataclass(frozen=True)
class Location:
    """Location for order"""
    latitude: float
    longitude: float

    def distance_to(self, other: 'Location', unit: str = 'km') -> float:
        """Calculate the distance to another location."""
        if unit == 'km':
            return distance((self.latitude, self.longitude),
                            (other.latitude, other.longitude)).kilometers
        elif unit == 'm':
            return distance((self.latitude, self.longitude),
                            (other.latitude, other.longitude)).meters
        else:
            raise ValueError("Invalid unit. Use 'km' or 'm'.")

    def is_nearby(self, other: 'Location', threshold: float, unit: str = 'km') -> bool:
        """Check if another location is nearby within a threshold distance."""
        _distance = self.distance_to(other, unit)
        return _distance <= threshold


if __name__ == '__main__':
    location1 = Location(-41.32, 174.81)
    location2 = Location(40.96, -5.50)
    print(location1.distance_to(location2, unit='m'))
