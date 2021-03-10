---
date: 03/02/2021
output: html
---
# Filtering Utilities
  
##### Table of Contents  
[deduplicate.py](#deduplicate.py)    
[filter_date.py](#filter_date.py)  
[filter_users.py](#filter_users.py)      
[gender.py](#gender.py)  
[geo.py](#geo.py)  
[geofilter.py](#geofilter.py)   
[noretweets.py](#noretweets.py)    
[sensitive.py](#sensitive.py)  
[search.py](#search.py)  
[twarc-archive.py](#twarc-archive.py)  
[webarchives.py](#webarchives.py)  

<a name="deduplicate.py"/>
 
## deduplicate.py
This utility removes tweets with duplicate IDs. According to the Twitter documentation, duplicate tweet ids are possible for tweets collected from the Twitter filter stream. 

Usage:

    python utils/deduplicate.py tweets.jsonl > deduped.jsonl
    
Arguments: 

    --extract-retweets 
    
For help: 

    python utils/deduplicate.py -h 
    
Output is a JSON containing the tweets without duplicate ids (i.e. the same tweet). Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.  

<a name="filter_date.py"/>

## filter_date.py
This utility filters out all tweets after min and/or max date given. 

Usage: 

    python utils/filter_date.py --mindate 1-may-2014 tweets.jsonl > filtered.jsonl
    
Arguments: 

    --mindate (provide mindate of tweets),
    --maxdate (provide max date of tweets) 
    
For help:

    python utils/filter_date.py -h 
    
Output is a JSON of tweets within the given min and/or max date(s) given. Specification of an output file is not necessary, however, without specification, output will be printed to the cmd. 

## filter_users.py 
This utility filters tweets posted by a list of users. The list should be supplied in a file which can contain the following, each on a separate line:
Screen names
User ids
Screen name, user id
User id, screen name

For issues with the input file visit: https://github.com/DocNow/twarc/issues/233

Usage: 

    python utils/filter_users.py screen_names.txt filtered_users.jsonl
    
Arguments:

    --neg-match (to filter out tweets NOT made by list of users)
 
For help:

    python utils/filter_users.py -h 
    
Output is a JSON of tweets made by those users as supplied in the data file . Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.  

## gender.py 
This utility filters tweets based on Twitter's guess about the gender of the user. 

Usage: 

    python utils/gender.py --gender female tweets.jsonl | utils/wordcloud.py > tweets-female.html python utils/gender.py --gender [male|female|unknown] tweet_file *
    
Arguments: 

    --gender male
    --gender female
    --gender unknown
    
For help:

    python utils/gender.py -h 

Output is a JSON of tweets filtered by specified gender. Specification of an output file is not necessary, however, without specification, output will be printed to the cmd. 

## geo.py 
This utility filters tweets and retweets based on the presence or absence of geocoding. 

Usage: 

    python utils/geo.py tweets.jsonl > tweets_geo.jsonl

Output is a JSON of tweets that have geocoding (no option for the negative -- i.e. tweets without geocoding). Specification of an output file is not necessary, however, without specification, output will be printed to the cmd. 

## geofilter.py 
This utility filters tweets by presence or absence of geo coordinates. 

Before use: 
    
    pip install Shapely 
    
Usage: 

    python utils/geofilter.py tweets.jsonl --yes-coordinates > tweets_with_geocoords.jsonl
    
Arguments: 

    --yes-coordinates (filter when geo coordinates are present)
    --yes-place (same as --yes-coordinates)
    --no-coordinates (filter when geo coordinates are not present)
    --no-place (same as --no-coordinates)
    --fence (geojson file with geofence, a virtual perimeter for a real-world geographic area)
    
For help:

    python utils/geofilter.py -h for help
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

## noretweets.py
In just about every dataset, the retweets will far outnumber the original tweets. This utility removes those retweets from the data. 

Usage:

    python utils/noretweets.py tweets.jsonl > tweets_noretweets.jsonl
 
Output is a JSON file containing the original data without the retweets. Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

## sensitive.py 
Twitter’s Media Settings page defines sensitive tweets as content that others may not wish to see such as violence or nudity. The API creates a variable in the metadata called “possibly_sensitive” representing a BOOLEAN value of TRUE or FALSE (where TRUE means the tweets IS possibly sensitive). This utility filters tweets based on the presence or absence of sensitive tweets. 

Usage: 

    python utils/sensitive. py tweets.jsonl > sensitive_tweets.jsonl
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

## search.py 
Filters tweet JSON based on a regular expression to apply to the test of the tweet. (The regular expression in the usage example below is ‘today’)

Usage: 

    python utils/search.py today tweets.jsonl > search.txt
    
Arguments: 

    -i (insensitive case match)
    
 For help: 

    python utils/search.py today -h

Specification of an output file is not necessary, however, without specification, output will be printed to the cmd

## twarc-archive.py 
Uses twarc to write Twitter search results to a directory of your choosing. Uses previous results to determine when to stop searching. For example, when you want to output search results for tweets mentioning “ferguson” to the directory /mnt/tweets/ferguson 

Usage: 

    % twarc-archive.py ferguson /mnt/tweets/ferguson
    
Arguments: 

    --consumer_key CONSUMER_KEY
    --consumer-token ACCESS TOKEN
    --access_token_secret ACCESS_TOKEN_SECRET
    --profile PROFILE -c CONFIG
    --tweet_mode {compat, extended}
    --twarc_command {search, timeline} search archive_dir

For help:

    python utils/twarc-archive.py -h
    
The first run will search twitter for tweets matching “ferguson” and write them to a file /mnt/tweets/ferguson/tweets-001.jsonl.gz. The second run will get the first tweet id in the output file and use it to write another file including any new tweet since that tweet.

## webarchives.py 

This utility filters tweets that contain links to a web archive. At the moment it supports archive.org and archive.is.

Usage: 
    
    python utils/webarchives.py tweets.json
    
Output is a JSON file with the tweets containing links to a web archive. 
