from requests_oauthlib import OAuth1Session
import os

class TwitterUtil:
    # def __init__(self, bearer_token=cf.BEARER_TOKEN, consumer_key=cf.API_KEY, 
    #             consumer_secret=cf.API_KEY_SECRET, access_token=cf.CLIENT_ID, access_token_secret=cf.CLIENT_SECRET):
    def __init__(self, consumer_key=os.environ["API_KEY"], consumer_secret=os.environ["API_KEY_SECRET"], access_token=os.environ["ACCESS_TOKEN"], access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]):
        self.auth = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

    def tweet(self, content):
        resource_url = r'https://api.twitter.com/2/tweets' #エンドポイントURL

        params = {
            "text":content
        }

        res = self.auth.post(resource_url,json=params)
        dict_results = {'code':res.status_code,
                        'response':res.json()}

        return dict_results