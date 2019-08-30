from picamera import PiCamera
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

ximage = ('image.jpg');


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


message = (edate + etime + ximage)

twitter.update_status(status=message)
print("Tweeted: %s" % message)
