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

<a name="intro"/>

--------------------------------THIS PAGE IS CURRENTLY UNDER CONSTRUCTION------------------------------

For the worked example, we will run through the [2019 Nipsey Hussle Funeral Tweets](https://archive.org/details/nipsey-hustle-tweets). The tweet ids are available under Downloadable Options on the right-hand side of the page and are named nipsey-ids.txt.gz. (Note: The extension .gz is a file format and software application used for file compression and decompression. If you don't know how to open this type of file or are having trouble doing so, visit Utilities Home and scroll to Resources). 

If you have not downloaded Twarc, do so at the [Twarc Doc Now](https://github.com/DocNow/twarc).

Once twarc is downloaded, move into your twarc directory then start the twarc session (using _twarc configure_ in the command line)

You are encouraged, but not required, to try out these utilities on your own before viewing the worked example code and outputs. Revisit the utility page corresponding to each section for an explanation of each utility. 

<a name="prep"/>

## Prepping the Data

The first step will be to unzip our dataset. It should unzip to a txt file titled ids.txt. For organizational purposes, we will rename this file nh_ids.txt for Nispey Hussle. You can keep the name ids.txt or modify it to fit your needs.

There are 11,642,103 ids listed in ids.txt. This amount of data is normally great for analysis because it gives us so much to work with. However, it also takes a long time to process. For this example, we will only be looking at the first 20,000 tweets. For ease of use, I have written the python code to do this. Click 'View on Github' at the top of this page or visit the [ucsb-collaboratory twarc repository](https://github.com/ucsb-collaboratory/twarc) to download the file subset.py. Once downloaded, simply run subset.py to appy it to your ids file. Look at the code documentation for more explanation of what it does and how it works. The outputted file is titled nh_sub_ids.txt. 

Next we will need to rehydrate the dataset. This can be done using the following command:

    twarc hydrate nh_sub_ids.txt > nh_sub_tweets.jsonl
    
*Note: If an account or tweet has been deleted from Twitter, it cannot be rehydrated. We will discuss this more later on*

<a name="filter"/>


## Filtering the Data 

Filtering the data can be seen as a way to clean the data before analysis.


### _deduplicate.py_

We'd like to start out by removing duplicate ids and retweets from our dataset using _deduplicate.py_.

    python utils/deduplicate.py --extract-retweets nh_sub_tweets.jsonl > nh_sub_dedup.jsonl
    

### _filter_date.py_

Then we want to look at tweets made the day of Nipsey Hussle death (March 31st, 2019) and the days following. We can do so using _filter_date.py_.

    python utils/filter_date.py --mindate 31-march-2019 nh_sub_dedup.jsonl > nh_sub_dod.jsonl
    

![DOD FILTER BY DATE](/assets/dod_filter_date.png)


As we can see from the photo of the CSV (We can use the json2csv.py utility listed on the Visualization page and demonstrated below to check this utility and those following), the first tweet entries are from the DOD. Since we took a smaller sample of the dataset, using this filter allows us to only analyze tweets made on the DOD as our subset doesn't extend beyond March 31st. 
    

### _filter_users.py_
   
This one can be a little tricky if the input file doesn't have proper formatting. The input must be supplied as a list in a TXT or CSV file. It can contain:

   screen names  
   user ids  
   screen name,user id  
   user id,screen name  
   
each on a separate line.

We're going to use screen names for this example. We can collect these using json2csv.py utility (see Visualization page or example below for more information). 


![DOD FILTER BY USERS INPUT1](/assets/dod_filter_users_input1.png)


We can then copy the screen names (in this case, the first _ screen names listed) into our file of choice. 


![DOD FILTER BY USERS INPUT2](/assets/dod_filter_users_input2.png)


Once we run our usage command, we will get a JSON containing only the tweets made by the screen names we listed in the file. 
 
    python utils/filter_users.py nh_sub_sn.txt nh_sub_dod.jsonl > nh_sub_users.jsonl
    

![DOD FILTER BY USER](/assets/dod_filter_users.png)
    

_gender.py__

    python utils/gender.py --gender female tweets.jsonl | utils/wordcloud.py > tweets-female.html python utils/gender.py --gender [male|female|unknown] tweet_file *
    
    
### _geo.py_ 

    python utils/geo.py nh_sub_dod.jsonl > nh_sub_geo.jsonl
    
    
![DOD GEO](/assets/dod_geo.png)


Based on our results, there are only two tweets in our sample dataset (after being filtered by DOD) that contain geo coordinates. 
    

### _geofilter.py_ 

By specifying that we want to filter by tweets without geo coordinates, we can get the tweets not returned by geo.py. 

    python utils/geofilter.py nh_sub_dod.jsonl --no-coordinates > nh_sub_geofilter.jsonl
  

![DOD GEO FILTER](/assets/dod_geo_filter.png)

    
### _noretweets.py_

    python utils/noretweets.py nh_sub_dod.jsonl > nh_sub_noretweets.jsonl
    
*Note: for the current dataset, this will just return our original dataset since there are no retweets*


### _sensitive.py_
    
    python utils/sensitive.py nh_sub_dod.jsonl > nh_sub_sensitive.jsonl
    
Column R is the variable possibly_sensitive, a boolean value (TRUE or FALSE) representing whether the tweet is considered sensitive. This first image is the dataset before running the utility sensitive.py. 
    

![DOD NOT SENSITIVE](/assets/dod_notsensitive.png)


The tweet that had been identified as sensitive has now been removed. 


![DOD SENSITIVE](/assets/dod_sensitive.png)
    

### _search.py_

    python utils/search.py shot nh_sub_dod.jsonl > nh_sub_search.jsonl
    

![DOD SEARCH SHOT](/assets/dod_search.png)
    

<a name="extract"/>


## Extracting the Data


### _embeds.py_

    python utils/embeds.py nh_sub_dod.jsonl > nh_sub_embeds.txt
    

![DOD EMBEDS](/assets/dod_embeds.png)
    

### _emojis.py_    
    
    python utils/emojis.py nh_sub_dod.jsonl > nh_sub_emojis.txt
    

![DOD EMOJIS](/assets/dod_emojis.png)
    

### _extractor.py_

    python utils/extractor.py user:screen_name entities:hashtags -output nh_sub_extractor.csv


![DOD EXTRACTOR](/assets/dod_extractor.png)


### _flakey.py_

    python utils/flakey.py nh_sub_ids.txt > nh_sub_flakey.csv
    
  
![DOD FLAKEY](/assets/dod_flakey.png)

    
### _media_urls.py_
    
    python utils/media_urls.py nh_sub_dod.jsonl > nh_sub_media_urls.txt
    
![DOD MEDIA URLS](/assets/dod_media_urls.png)
    

### _retweets.py_
    
    python utils/retweets.py nh_sub_dod.jsonl > nh_sub_retweets.jsonl
    
This returns a blank JSON because there are no retweets in the subsetted dataset filtered by date. However, when we run this on the original subsetted dataset:
    
    python utils/retweets.py nh_sub_tweets.jsonl > nhsub_retweets.jsonl
    

![DOD RETWEETS](/assets/dod_retweets.png)


### _tags.py_
    
    python utils/tags.py nh_sub_dod.jsonl > nh_sub_hashtags.txt
    

![DOD TAGS](/assets/dod_tags.png)
    

### _times.py_
    
    python utils/times.py nh_sub_dod.jsonl > nh_sub_times.txt
    

![DOD TIMES](/assets/dod_times.png)
    

_tweets.py_
  
    python utils/tweets.py nh_sub_dod.jsonl > nh_sub_tweets.txt
    
### _tweetometer.py_
 
    python utils/tweetometer.py nh_sub_dod.jsonl > nh_sub_tweetometer.csv
    
![DOD TWEETOMETER](/assets/dod_tweetometer.png)
    
### _tweet_text.py_
    
    python utils/tweet_text.py nh_sub_dod.jsonl > nh_sub_tweet_text.txt
    
![DOD TWEET TEXT](/assets/dod_tweet_text.png)
    
### _tweet_urls.py_
    
    python utils/tweet_urls.py nh_sub_dod.jsonl > nh_sub_tweet_urls.txt
    
![DOD TWEET TEXT](/assets/dod_tweet_urls.png)
    
### _users.py_
    
    python utils/users.py nh_sub_dod.jsonl > nh_sub_users.txt
    
 ![DOD TWEET TEXT](/assets/dod_users.png)   

<a name="visual"/>

## Visualizing the Data

This section allows us to create visuals of the data. 

### _geojson.py_

We can use geojson.py to create a GeoJSON file when the geospatial location of a tweet is available.  


    python utils/geojson.py nh_sub_dod.jsonl > nh_dod_geojson.geojson 
    
We can then use a [GeoSpatial JSON reader](http://geojsonviewer.nsspot.net/) to visualize this file on the map.  
    
![DOD GEOJSON](/assets/dod_geojson.png)

We can do further manipulation by creating a centroid instead of a bounding box.

    python utils/geojson.py --centroid nh_sub_dod.jsonl > nh_dod_centroid.geojson
    
![DOD CENTROID GEOJSON](/assets/dod_centroid.png)

Or we can add a random lon and lat shift to the bounding box centroids (0-0.1)

    python utils/geojson.py --centroid --fuzz 0.01 nh_sub_dod.jsonl > nh_dod_fuzz.geojson
    
![DOD FUZZ GEOJSON](/assets/dod_fuzz.png)

As we can see below, the shift is not too big.

![DOD CENTROID VS FUZZ GEOJSON](/assets/dod_centroidvsjson.png)
    
*Jon's tidbit about mapping Twitter*
   
### _json2csv.py_

We can view the tweets in a more cohesive manner by turning our json into a csv. 

*Note: if you're using Windows and you get a charmap error, you can change your Region settings using the instructions [here](https://scholarslab.github.io/learn-twarc/08-win-region-settings)*

    python utils/json2csv.py nh_sub_dod.jsonl > nh_dod_tweets.csv
    
 ![DOD CSV](/assets/dod_json2csv.png)
    
### _network.py_

    python utils/network.py nh_sub_dod.jsonl nh_dod_network.html
    
![DOD NETWORK](/assets/dod_network.png)

We can click on the dots to see the individual tweets. The central node(red) is the original tweet of a video interview. The connected nodes(yellow) are the replies and retweets to/of that video. The other nodes(gray) are attached by similarity to that central node and it's surrounding nodes. 

![DOD NETWORK VIDEO](/assets/dod_network_video.gif)

We can move the cluster by clicking on one of the nodes and dragging it to the place on our screen we would like it to be. The bigger the data size, the longer it will take to mode the nodes around. There are also nodes not attached to the cluster. 

### _source.py_

We can create a page with the sources(ranked most to least) used with source.py.

    python utils/source.py nh_sub_dod.jsonl > nh_dod_source.html
    
*Note: The html is hardcoded in the source.py file. The title of the page is set to 'Title Here'. To change this, you have to edit the html code itself from ['Title Here'](https://github.com/DocNow/twarc/blob/3dd763516e643d070fab237bd5fb18b1274ec738/utils/wall.py#L113) to the title of your choice*  
    
   
![DOD SOURCE](/assets/dod_source.png)


We can click on the links provided for each source to learn more about them. 
  

### _wall.py_

We can also create a wall of tweets. 

    python utils/wall.py nh_sub_dod.jsonl > nh_dod_wall.html
    

![DOD WALL](/assets/dod_wall.png)
   

### _wordcloud.py_    

The last visualization tool we'll go over is creating a wordcloud. 
    
    python utils/wordcloud.py nh_sub_dod.jsonl > nh_dod_wordcloud.html
    

![DOD WORDCLOUD](/assets/dod_wordcloud.png)


<a name="status"/>

## Getting the Status the Data

    
### _deleted_users.py    

We can run deleted_users.py to produce a JSON containing the tweets that have been deleted. 
    
    python utils/deleted_users.py nh_sub_dod.jsonl > nh_dod_deleted_users.jsonl
   
   
![DOD DELETED USERS](/assets/dod_deleted_users.png)
   
   
### _deletes.py_    

We can then feed the output JSON into deletes.py to see the reason the tweet has been deleted. 
    
    python utils/deletes.py nh_dod_deleted_users.jsonl > nh_dod_deletes.txt
    
    
![DOD DELETES](/assets/dod_deletes.png)


### _foaf.py_ 
   
    python utils/foaf.py 2267720350
    
%Just trying to figure out how to open the SQL file%

### _oembeds.py_
    
    python utils/oembeds.py nh_sub_dod.jsonl > nh_dod_oembeds.jsonl
    
*Note: Warning messages like the following will be printed to the command line if the url has been deleted.*     
    
 
![DOD OEMBEDS WARNING](/assets/dod_oembeds_warning.png)

    
### _tweet.py_

We'll use the first tweet id in our dataset. 
    
![DOD TWEET ID](/assets/dod_tweet_id.png)
    
    python utils/tweet.py 1112143431197835264 > 1tweet.jsonl

 
### _tweet_compliance.py_
    
    python utils/tweet_compliance.py nh_dod_ids.txt > nh_sub_dod.jsonl > dod_tweet_compliance.jsonl
    
The current tweets will be output to a dod_tweet_compliance.jsonl.
    
![DOD TWEET COMPLIANCE](/assets/dod_tweet_compliance.png)

The ids of tweets that are not available are output to the command line along with the deleted tweets. 


![DOD TWEET COMPLIANCE](/assets/dod_tweet_compliance1.png)

    
_wayback.py_
    
    python utils/wayback.py tweets.jsonl > wayback.txt

<a name="organize"/>


## Organizing the Data


### _sort_by_id.py_

This one is pretty simple. It just sorts the dataset in ascending order by id. It's essentially the same as sorting by date as tweet ids are parsed out in order of creation.

    python utils/sort_by_id.py nh_sub_dod.jsonl > nh_dod_sort_by_id.jsonl
    
_unshrtn.py_    
    
    cat tweets.jsonl | utils/unshrtn.py > unshortn.jsonl
    
_urls.py_
    
    cat unshortn.jsonl | utils/urls.py | sort | uniq -c | sort -nr > urls.txt
   
_youtubedl.py_
   
    python utils/youtubedl.py nh_sub_dod.jsonl
 
 
[Back To Top](#worked-example)

