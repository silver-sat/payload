

import logging
from http.client import HTTPConnection  # py3
import datetime, json

# Log requests made by Twython to twitter
log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)
HTTPConnection.debuglevel = 1

import requests
from twython import Twython

class Twitter(Twython):
    def __init__(self,*args,**kwargs):
        self.httpsproxy = None
        if kwargs.get('httpsproxy'):
            self.httpsproxy = kwargs.get('httpsproxy')
            del kwargs['httpsproxy']
        Twython.__init__(self,*args,**kwargs)
        if self.httpsproxy:
            self.client.get = self.myget
            self.client.post = self.mypost
    def monkeypatch(self,method,url,**kwargs):
        req = self.client.prepare_request(
            requests.Request(method=method,
                             url=url,
                             auth=self.client.auth,
                             headers=self.client.headers,
                             **kwargs))
        headers = {'Host': 'api.twitter.com'}
        headers.update(self.client.headers)
        headers.update({'Authorization': req.headers['Authorization']})
        url = 'http://' + self.httpsproxy + '/' + url.split('/',3)[-1]  
        return url,headers
    def myget(self,url,**kwargs):
        url,headers = self.monkeypatch('get',url,**kwargs)
        return requests.get(url,headers=headers,**kwargs)
    def mypost(self,url,**kwargs):
        url,headers = self.monkeypatch('post',url,**kwargs)
        return requests.post(url,headers=headers,**kwargs)

# Known as API key on twitter website
consumer_key        = ''
# Known as API secret key on twitter website
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

twitter = Twitter(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    httpsproxy='localhost:8383'
)

retval = twitter.verify_credentials()
print(json.dumps(retval,indent=2))

message = "[%s] Hello World!"%(datetime.datetime.now().ctime(),)
retval = twitter.update_status(status=message)
print(json.dumps(retval,indent=2))