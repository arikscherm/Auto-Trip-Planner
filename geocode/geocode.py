from geopy.geocoders import Nominatim
def get_coordinates(input):
    geolocator = Nominatim(user_agent="here")
    location = geolocator.geocode(input)
    try:
        coordinates = (location.latitude, location.longitude)
        return coordinates
    except:
        print("Location not found, please try again.")

