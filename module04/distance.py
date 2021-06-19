import math

RADIUS_EARTH: float = 6371.01


def distance_between_cities(lat1: float, lon1: float, lat2: float = 51.5072, lon2: float = -0.1275) -> float:
    def calculate_distance():
        nonlocal lat1, lon1, lat2, lon2
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)

        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)
        result = RADIUS_EARTH * math.acos(
            math.sin(lat1) * math.sin(lat2)
            + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)
        )
        return result

    distance: float = calculate_distance()
    return distance


if __name__ == '__main__':
    print(distance_between_cities(lon1=30.523, lat1=50.45))
