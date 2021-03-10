---
date: 03/08/2021
output: html
---
#### Table of Contents 
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
## deletes.py
## deleted_users.py
## foaf.py
## oembeds.py
## tweet.py 
## tweet_compliance.py
## wayback.py

deleted.py: checks the status of each tweet, outputting tweets that have been deleted
deletes.py: takes deleted tweet output and determines why tweet/user was deleted
deleted_users.py: checks the status of each tweet, outputting tweets/users that have been deleted
foaf.py: finds the friend of a friend network for a particular user
oembeds.py: reads a stream of tweet JSON and augments .entities.urls with oembed metadata for the URL
tweet.py: fetches tweet from twitter stream using tweet id, if it exists
tweet_compliance.py: provides most recent version of a tweet, if it exists
wayback.py: reads stream of tweets and checks whether that tweet is archived at Internet Archive
