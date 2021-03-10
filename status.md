---
date: 03/08/2021
output: html
---
##### Table of Contents 
[deleted.py](#headers)  
[deletes.py](#deletes.py)  
[deleted_users.py](#deleted_users.py)
[foaf.py](#foaf.py)   
[oembeds.py](#oembeds.py) 
[tweet.py ](#tweet.py) 
[tweet_compliance.py](#tweet_compliance.py)  
[wayback.py](#wayback.py)

<a name="headers"/>
 
## deleted.py
This utility reads in tweets, rehydrates them, and only outputs the tweets JSON for tweets that are no longer available.

Usage: 

    python utils/deleted.py tweets.jsonl > deleted.jsonl
    
## deletes.py
This utility takes a JSON of deleted tweets/users (can use output from deleted_users.py or deleted.py) and outputs the reason the tweet was deleted. Lookups are based on user id so it may give different results than when lookups are done through screen name. 

Usage: 

    python utils/deletes.py tweet.jsonl > deletes.jsonl
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd. 

## deleted_users.py
This utility outputs the tweets made by deleted users from a JSON to a new JSON. The output to cmd will be warning messages with the tweet users that have been deleted.

Usage: 

    python utils/deleted_users.py tweets.jsonl > deleted_users.jsonl

## foaf.py
This utility gets the friend-of-a-friend network for a particular user. The network is expressed as tuples of user identifiers for the user and their friend (who they follow). Input is the user's id. 

Usage: 

    python utils/foaf.py 2267720350
    
Arguments: 

    --level (how far out in the social group to follow)

For help: 

    python utils/foaf.py -h

## oembeds.py
This utility reads a stream of tweet JSON and augments .entities.urls with oembed metadata for the URL using the oembedders python module and a sqlite database to prevent multiple lookups for the same URL. This module can be installed using the command:

    pip install oembedders
    
For more information on the module, see https://github.com/edsu/oembedders. For an example of augmentation see https://github.com/DocNow/twarc/blob/main/utils/oembeds.py.

Usage: 

    python utils/oembeds.py election.jsonl > oembeds.jsonl
    
Note: Warning messages may be printed to the screen if URLs provided are no longer valid/available (i.e. if the URL is for a YouTube video that has been deleted)

## tweet.py 
This utility fetches a single tweet when given a tweet id.

Usage: 

    python utils/tweet.py 795847322957512704 > tweet.txt
    
OR

    python utils/tweet.py 795847322957512704 > tweet.jsonl
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

For help:  

    python utils/tweet.py -h

## tweet_compliance.py
This utility provides the most recent version of a tweet and removes tweets that are unavailable (deleted or protected) tweets. This utility is also useful for splitting out available tweets from unavailable tweets. For each tweet in a list of tweets or tweet ids provided by standard input or contained in files, it looks up the current state. If tweet is not available and tweet ids are provided, the tweet id is output to standard error. If a tweet is not available and tweets are provided, the (deleted) tweet is output to standard error. Otherwise the current tweet (i.e. the tweet retrieved from the API) is returned to standard out. Ordering is not guaranteed. See https://developer.twitter.com/en/docs/tweets/compliance/overview for more information on tweet compliance. 

Usage: 

    python utils/tweet_compliance.py test.txt > test.json 2> test_delete.txt

Specification of an output file is not necessary, however, without specification, output will be printed to the cmd

## wayback.py
This utility reads a stream of tweets and checks to see if the tweet is archived at Internet Archive and optionally requests SavePageNow save it. 

Usage: 

    python utils/wayback.py tweets.jsonl > wayback.txt
