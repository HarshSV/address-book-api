from geopy.distance import geodesic

def is_within_distance(lat1, lon1, lat2, lon2, distance_km):
    return geodesic((lat1, lon1), (lat2, lon2)).km <= distance_km