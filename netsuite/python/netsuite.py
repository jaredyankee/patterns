import os
import requests
from requests_oauthlib import OAuth1
from oauthlib.oauth1 import SIGNATURE_HMAC_SHA256

# returns valid auth object for netsuite requests using .env creds
# see .env.example
def ns_auth ():
    return OAuth1(
        client_key=os.environ["ns_consumer_key"],
        client_secret=os.environ["ns_consumer_secret"],
        resource_owner_key=os.environ["ns_token_id"],
        resource_owner_secret=os.environ["ns_token_secret"],
        signature_method=SIGNATURE_HMAC_SHA256,
        realm=os.environ["ns_realm"],
    )

def ns_request (method, url, body=None, **kwargs):
    response = requests.request(
        method=method,
        url=url,
        auth=ns_auth()
        json=body
        headers={}
    )
    response.raise_for_status()
    return response