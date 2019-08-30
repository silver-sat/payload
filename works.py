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

from names_works import (
    postme
    )
    

myimage = ('/home/pi/Desktop/image.jpg');


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


message = (postme + edate  + etime)
#twitter.update_status(status=message)


photo = open(myimage, 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=message, media_ids=[response['media_id']])
print("Tweeted: %s with image %s" % (message, myimage))
