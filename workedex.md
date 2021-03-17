---
date: 2021-03-15
output: html
---
[Utilities Home](utilities.md) • [Filtering](filtering.md) • [Extraction](extraction.md) • [Visualization](visualization.md) • [Status](status.md) • [Organization](organization.md) • [System](system.md)

# Worked Example

##### Table of Contents  
[Intro](#intro)  
[Prepping the Data](#prep)  
[Filtering the Data](#filter)  
[Extracting Data](#extract)  
[Visualizing the Data](#visual)  
[Getting the Status of the Data](#status)  
[Organzing the Data](#organize)  
[Checking Your System](#system)  

<a name="intro"/>

For the worked example, we will run through the [2019 Nipsey Hussle Funeral Tweets](https://archive.org/details/nipsey-hustle-tweets). The tweet ids are available under Downloadable Options on the right-hand side of the page and are named nipsey-ids.txt.gz. (Note: The extension .gz is a file format and software application used for file compression and decompression. If you don't know how to open this type of file or are having trouble doing so, visit Utilities Home and scroll to Resources). 

If you have not downloaded Twarc, do so at the [Twarc Doc Now](https://github.com/DocNow/twarc). For a more non-technical-user download, visit [scholarslab](https://scholarslab.github.io/learn-twarc/06-twarc-command-basics.html). Once Twarc is downloaded, be sure to start the twarc session. 

You are encouraged, but not required, to try out these utilities on your own before viewing the worked example code and outputs. Revisit the utility page corresponding to each section for in-depth explanation of each utility. 

<a name="prep"/>

## Prepping the Data

The first step will be to unzip out dataset. It should unzip to a txt file titled ids.txt. For organizational purposes, we will rename this file nh_ids.txt for Nispey Hussle. You can keep the name ids.txt or modify it to fit your needs.

There are 11,642,103 ids listed in ids.txt. This amount of data is normally great for analysis because it gives us so much to work with. However, it also takes a long time to process. For this example, we will only be looking at the first 20,000 tweets. For ease of use, I have written the python code to do this. Click 'View on Github' at the top of this page or visit the [ucsb-collaboratory twarc repository](https://github.com/ucsb-collaboratory/twarc) to download the file subset.py. Once downloaded, simply run subset.py to appy it to your ids file. Look at the code documentation for more explanation of what it does and how it works. The outputted file is titled nh_sub_ids.txt. 

Next we will need to rehydrate the dataset. This can be done using the following command:

    twarc hydrate nh_sub_ids.txt > nh_sub_tweets.jsonl
    
*Note: If an account or tweet has been deleted from Twitter, it cannot be rehydrated. We will discuss this more later on*

<a name="filter"/>

## Filtering the Data 

Filtering the data can be seen as a way to clean the data before analysis.

We'd like to start out by removing duplicate ids and retweets from our dataset using _deduplicate.py_.

    python utils/deduplicate.py --extract-retweets nh_sub_tweets.jsonl > nh_sub_dedup.jsonl

Then we want to look at tweets made the day of Nipsey Hussle death (March 31st, 2019) and the days following. We can do so using _filter_date.py_.

    python utils/filter_date.py --mindate 31-march-2019 nh_sub_dedup.jsonl > nh_sub_dod.jsonl
    
----------------------------------------------------------------------------UNDER CONSTRUCTION-----------------------------------------------------------------------------------  
_filter_users.py_
   
    python utils/filter_users.py nh_sub_sn.txt > nh_sub_users.jsonl
    
_gender.py__

    python utils/gender.py --gender female tweets.jsonl | utils/wordcloud.py > tweets-female.html python utils/gender.py --gender [male|female|unknown] tweet_file *
    
Now we're going to filter based on the presence of geo coordinates _geo.py_. 

    python utils/geo.py nh_sub_dod.jsonl > nh_sub_geo.jsonl
    
_geo.py_ 

    python utils/geofilter.py nh_sub_dod.jsonl --no-coordinates > nh_sub_geofilter.jsonl
    
_noretweets.py_

    python utils/noretweets.py nh_sub_dod.jsonl > nh_sub_noretweets.jsonl
    
_sensitive.py_
    
    python utils/sensitive.py nh_sub_dod.jsonl > nh_sub_sensitive.jsonl
    
_search.py_

    python utils/search.py rip nh_sub_dod.jsonl > nh_sub_search.txt
    
_twarc-archive.py_

    % twarc-archive.py rip /user/tweets/rip
    
_webarchives.py_

    python utils/webarchives.py nh_sub_dod.jsonl

<a name="extract"/>

## Extracting the Data

_embeds.py_

    python utils/embeds.py nh_sub_dod.jsonl > nh_sub_embeds.txt
    
_emojis.py_    
    
    python utils/emojis.py nh_sub_dod.jsonl > nh_sub_emojis.txt
    
_extractor.py_

    python utils/extractor.py user:screen_name -output nh_sub_extractor.csv
    
_flakey.py_

    python utils/flakey.py nh_sub_ids.txt > nh_sub_flakey.csv
    
_media_urls.py_
    
    python utils/media_urls.py nh_sub_dod.jsonl > nh_sub_media_urls.txt
    
_media2warc.py_

    python utils/media2warc.py /user/tweets/rip/nh_sub_dod-0001.jsonl.gz /user/tweets/rip/nh_sub_dod-0001.warc.gz
    
_retweets.py_
    
    python utils/retweets.py nh_sub_dod.jsonl > nh_sub_retweets.jsonl
    
_tags.py_
    
    python utils/tags.py nh_sub_dod.jsonl > nh_sub_hashtags.txt
    
_times.py_
    
    python utils/times.py nh_sub_dod.jsonl > nh_sub_times.txt
    
_tweets.py_
  
    python utils/tweets.py nh_sub_dod.jsonl > nh_sub_tweets.txt
    
_tweetometer.py_
 
    python utils/tweetometer.py nh_sub_dod.jsonl > nh_sub_tweetometer.csv
    
_tweet_text.py_
    
    python utils/tweet_text.py nh_sub_dod.jsonl > nh_sub_tweet_text.txt
    
_tweet_urls.py_
    
    python utils/tweet_urls.py nh_sub_dod.jsonl > nh_sub_tweet_urls.txt
    
_users.py_
    
    python utils/users.py nh_sub_dod.jsonl > nh_sub_users.txt

<a name="visual"/>

## Visualizing the Data

<a name="status"/>

## Getting the Status the Data

<a name="organize"/>

## Organizing the Data

<a name="system"/>

## Checking Your System


[Back To Top](#worked-example)
