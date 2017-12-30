""" Extract location for this tweet, depending on tweet's coordinates, tweet's place and user's location"""
import src.config as config
import googlemaps

# TODO persist on disk or use Redis
location_cache = {}
gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)


def get_tweet_location(tweet):
    if tweet["coordinates"]:
        if tweet["coordinates"]["type"] == "Point":
            return tweet["coordinates"]["coordinates"]  # lng, lat
        else:
            print("Tweet with coordinates with type not Point" + str(tweet))
    elif tweet["place"]:
        bb = tweet["place"]["bounding_box"]
        if bb["type"] == "Polygon":
            coordinates = bb["coordinates"][0]
            lng = (coordinates[0][0] + coordinates[1][0] + coordinates[2][0] + coordinates[3][0]) / 4
            lat = (coordinates[0][1] + coordinates[1][1] + coordinates[2][1] + coordinates[3][1]) / 4
            return [lng, lat]
        else:
            print("Tweet with place with type not Polygon" + str(tweet))
    else:
        # Try to get location from the user's location
        user = tweet["user"]
        if user["location"]:
            return get_location_geo(user["location"])


def get_location_geo(location):
    """ return [lng, lat] for a location """
    if location in location_cache:
        return location_cache[location]
    else:
        google_geo = get_location_google_geo(location)
        if google_geo:
            location_cache[location] = google_geo
        return google_geo


def get_location_google_geo(location):
    """ Get location's geo Using Google maps API or return None"""
    geo_response = gmaps.geocode(location)
    if len(geo_response) > 0:
        geo_response = geo_response[0]
        geo = geo_response["geometry"]["location"]
        return [geo["lng"], geo["lat"]]
    else:
        print(str(location) + " Not found in Google")
        return None
