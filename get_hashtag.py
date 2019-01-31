#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import key

oath_key_dict = {
    "consumer_key": key.CONSUMER_KEY,
    "consumer_secret": key.CONSUMER_SECRET,
    "access_token": key.ACCESS_TOKEN,
    "access_token_secret": key.ACCESS_TOKEN_SECRET
}

def main():
    tweets = tweet_search("#python", oath_key_dict)
    sum_num_hash = 0
    for tweet in tweets["statuses"]:
        ##tweet_id = tweet[u'id_str']
        ##text = tweet[u'text']
        ##created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        ##screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        sum_num_hash += 1
    ##print("tweet_id:", tweet_id)
    ##print("text:", text)
    ##print("created_at:", created_at)
        ##print("user_id:", user_id)
        ##print("user_desc:", user_description)
    ##print("screen_name:", screen_name)
        ##print("user_name:", user_name)
    print(sum_num_hash)    
    return 


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
        oath_key_dict["consumer_key"],
        oath_key_dict["consumer_secret"],
        oath_key_dict["access_token"],
        oath_key_dict["access_token_secret"]
    )
    return oath


def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/tweets/search/30day/mashuhash.json"
    oath = create_oath_session(oath_key_dict)
    response = oath.get(url)
    if response.status_code != 200:
        print("Error code: %d" % (response.status_code))
        return None
    tweets = json.loads(response.text)
    return tweets


# Execute
if __name__ == "__main__":
    main()
