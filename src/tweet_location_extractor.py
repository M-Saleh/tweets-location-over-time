""" Extract location for this tweet, depending on tweet's coordinates, tweet's place and user's place"""


def get_tweet_location(tweet):
    if tweet["coordinates"]:
        if tweet["coordinates"]["type"] == "Point":
            return tweet["coordinates"]["coordinates"] # lng, lat
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
