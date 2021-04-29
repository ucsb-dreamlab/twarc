---
date: 03/08/2021
output: html
---
[Utilities Home Page](utilities.md) • [Filtering](filtering.md) • Extraction • [Visualization](visualization.md) • [Status](status.md) • [Organization](organization.md) • [System](system.md) • [Worked Example](workedex.md) • [Resources](resources.md)


# Extraction Utilities

##### Table of Contents  
[embeds.py](#embeds.py)  
[emojis.py](#emojis.py)  
[extractor.py](#extractor.py)  
[flakey.py](#flakey.py)  
[media_urls.py](#media_urls.py)  
[media2warc.py](#media2warc.py)  
[retweets.py](#retweets.py)  
[tags.py](#tags.py)  
[times.py](#times.py)  
[tweets.py](#tweets.py)  
[tweetometer.py](#tweetometer.py)  
[tweet_text.py](#tweet_text.py)  
[tweet_urls.py](#tweet_urls.py)  
[users.py](#users.py)  

<a name="embeds.py"/>

## embeds.py
This utility creates a list of media URLS used in the dataset. 

Usage:

    python utils/embeds.py tweets.jsonl > embeds.txt
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

<a name="emojis.py"/>

## emojis.py
This utility creates a text file with all the emojis in the data with the number of times each emoji has been used. Note: emojis and non-Latin characters may not render well because of certain UTF-8 characters, particularly in Windows. To fix this you can follow the directions [here](https://scholarslab.github.io/learn-twarc/08-win-region-settings).

Usage: 

    python utils/emojis.py tweets.jsonl > emojis.txt
    
Arguments: 
   
    -n NUMBER
    --number=NUMBER
    
For help: 

    python utils/emojis.py -h
    
<a name="extractor.py"/>

## extractor.py
This utility extracts supplied attributes from tweets. Parsing will be done using a default file, but you can specify the path with the argument -path PATH as listed below.

Usage: 

    python utils/extractor.py user:screen_name -output extractor.csv
    
Arguments:

    -dialect DIALECT (sets dialect for csv output. Defaults to excel. See python module csv.list_dialects())
    -string STRING (regular expression for files to parse. Defaults to empty string)
    -path PATH (optional path to folder containing tweets. Defaults to current folder)
    -output OUTPUT (optional file to output results. Defaults to output.csv)
    -start START (define start date for tweets. Format (mm:dd:yyyy)
    -end END (define end date for tweets. Format (mm:dd:yyyy)
    -hashtag HASHTAG (define a hashtag that must be in parsed tweets)
    attributes[attributes…] (attributes to search for. Attributes nested inside other attributes should be separated by a colon. Ex: user:screen_name, entities:hashtags:text)
    
For help: 

    python utils/extractor.py -h

<a name="flakey.py"/>

## flakey.py
This utility takes Snowflake ids (tweet ids) and extracts their creation times to a csv. More information about Snowflake ids and deleted tweets can be found  [here](https://ws-dl.blogspot.com/2019/08/2019-08-03-searching-web-archives-for.html)

Usage:

    python utils/flakey.py ids.txt > flakey.csv
    
<a name="media_urls.py"/> 
 
## media_urls.py
This utility creates a text file of the media URLs of images used in the data and the tweet ids that used them.

Usage: 

    python utils/media_urls.py tweets.jsonl > media_urls.txt

Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

<a name="media2warc.py"/>

## media2warc.py
This utility extracts media urls from tweet json.gz and saves them as warc records. [Warcio](https://github.com/webrecorder/warcio) is a dependency and before you can use it, you need to issue the following command:

    % pip install warcio

The input file will be checked for duplicate urls to avoid duplicates within the input file. Subsequent runs will be deduplicated using a sqlite db. If an identical-payload-digest is found a revist record is created.

Usage: 

    python utils/media2warc.py /mnt/tweets/ferguson/tweets-0001.jsonl.gz /mnt/tweets/ferguson/tweets-0001.warc.gz

Arguments:

    --threads <int> (allows script to fetch media resources in multiple threads (max 2)(default to a single thread))
  
Note: Please be careful modifying this script to use more than two threads since it can be interpreted as a DoS-attack 
    
<a name="retweets.py"/> 
 
## retweets.py
This utility prints out retweeted tweet ids and the number of times they have been retweeted

Usage: 

    python utils/retweets.py tweets.jsonl > retweets.jsonl
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.    

For help:

    python utils/retweets.py -h

<a name="tags.py"/>

## tags.py
This utility creates a text file of hashtags used in the data and the number of times each are used.

Usage: 

    python utils/tags.py tweets.jsonl > hashtags.txt

<a name="times.py"/>

## times.py
This utility extracts the creation time from each tweet in the data. 

Usage: 

    python utils/times.py tweets.jsonl > times.txt
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd
    
Arguments: 

    -f FORMAT 
    --format = FORMAT  
    -l, --local
    
For help:  

    python utils/times.py -h

<a name="tweets.py"/>

## tweets.py
This utility extracts the tweet user, screen_name, text, and id_str from each tweet in the data. 

Usage: 

    python utils/tweets.py tweets.jsonl > tweets.txt

Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

<a name="tweetometer.py"/>

## tweetometer.py
This utility reads a twitter user JSON and prints out CSV with the following information:
- When the user’s account was created
- How many tweets the account has sent to date
- The average number of tweets the user makes per given unit (default is hour)

Usage: 

    python utils/tweetometer.py tweets.jsonl > tweetometer.csv

Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

Arguments: 
    
    --unit (second, minute, hour, day, year)

For help:  

    python utils/tweetometer.py -h

<a name="tweet_text.py"/>

## tweet_text.py
This utility extracts the full text of each tweet with the user name of the account who created the tweet.

Usage: 

    python utils/tweet_text.py tweets.jsonl > tweet_text.txt
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.

<a name="tweet_urls.py"/>

## tweet_urls.py
This utiltiy extracts tweet id, screen name, retweet count, and tweet urls from each tweet.

Usage: 

    python utils/tweet_urls.py tweets.jsonl > tweet_urls.txt
    
OR

    python utils/tweet_urls.py tweets.jsonl > tweet_urls.jsonl
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd. Alternatively, output could be set as JSON. 

<a name="users.py"/>

## users.py
This utility outputs users one line at a time. 

Usage:

    python utils/users.py tweets.jsonl > users.txt
    
Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.
    
Use bash to count unique users:

    sort users.txt | uniq -c | (sort gives you a list of IDs sorted by how many tweets are in your dataset.)
        
[Back To Top](#extraction-utilities)
