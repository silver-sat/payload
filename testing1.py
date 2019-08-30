from twython import Twython
import time

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

from etime import (
    etime,
    edate
)


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


message = (etime edate)

twitter.update_status(status=message)
print("Tweeted: %s" % message)

