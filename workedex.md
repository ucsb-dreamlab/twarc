---
date: 2021-03-15
output: html
---
[Utilities Home](utilities.md) • [Filtering](filtering.md) • [Extraction](extraction.md) • [Visualization](visualization.md) • [Status](status.md) • [Organization](organization.md) • [System](system.md) • Worked Example • [Resources](resources.md)

#  Worked Example

##### Table of Contents  
[Intro](#intro)  
[Prepping the Data](#prep)  
[Filtering the Data](#filter)  
[Extracting Data](#extract)  
[Visualizing the Data](#visual)  
[Getting the Status of the Data](#status)  
[Organzing the Data](#organize)  

<a name="intro"/>   

*This worked example does not cover basic twarc setup and configuration. If you have not installed twarc, do so at the [twarc DocNow](https://github.com/DocNow/twarc) or on the updated [twarc documentation page](https://twarc-project.readthedocs.io/en/latest/) has been moved.*   

You are encouraged, but not required, to try out these utilities on your own before viewing the worked example code and outputs. Visit the [Utilities Home page](utilities.md) and the corresponding sections for an explanation of each utility, as well as parameters available that are not included in this worked example.  

For the worked example, we will run through the [2019 Nipsey Hussle Funeral Tweets](https://archive.org/details/nipsey-hustle-tweets). The tweet ids are available under Downloadable Options on the right-hand side of the page and are named nipsey-ids.txt.gz. (Note: The extension .gz is a file format and software application used for file compression and decompression. If you don't know how to open this type of file or are having trouble doing so, visit [Resources](resources.md)). 


<a name="prep"/>

## Prepping the Data

The first step will be to unzip our dataset. It should unzip to a txt file titled ids.txt. For organizational purposes, we will rename this file nh_ids.txt for Nispey Hussle. You can keep the name ids.txt or modify it to fit your needs. See [Resources](resources.md) for help on unzipping the txt.gz file. 

There are 11,642,103 ids listed in nh_ids.txt. This amount of data is normally great for analysis because it gives us so much to work with. However, it also takes a long time to process. For this example, we will only be looking at the first 20,000 tweets. For ease of use, I have written the python program [subset.py](https://github.com/ucsb-collaboratory/twarc/subset.py) to do this. Look at the code documentation for more explanation of what it does and how it works. We will title our ouputted file nh_sub_ids.txt. 

*Alternatively, see the python program [random_subset.py](https://github.com/ucsb-collaboratory/twarc/random_subset.py) to create a subset of random tweet ids.* 

Next we will need to rehydrate the dataset.

    twarc hydrate nh_sub_ids.txt > nh_sub_tweets.jsonl
    
*Note: If an account or tweet has been deleted from Twitter, it cannot be rehydrated.*


<a name="filter"/>


## Filtering the Data 

Filtering the data can be seen as a way to clean the data before analysis.


### _deduplicate.py_

We'd like to start out by removing duplicate ids and retweets from our dataset.


    python utils/deduplicate.py nh_sub_tweets.jsonl > nh_sub_deduplicate.jsonl
    
    
We can also run 


    python utils/deduplicate.py --extract-retweets nh_sub_tweets.jsonl > nh_sub_dedupretweets.jsonl
    
    
to extract just the retweets to a new JSON. 
    

### _filter_date.py_

Then we want to look at tweets made the day of Nipsey Hussle death (March 31st, 2019). This might not limit the date to only March 31st, 2019 with a bigger dataset (or when using random_subset.py) because you can only specify a min or a max date. If you would like to limit the date, you will have to run _filter_date.py_ twice: the first time filtering by mindate OR maxdate, and the second time filtering the ouputted dataset by the remaining parameter. For our current dataset, this works because the tweets only date up to March 31st so by specifying a mindate, we are only left with tweets made on March 31st, 2019.   


    python utils/filter_date.py --mindate 31-march-2019 nh_sub_deduplicate.jsonl > nh_dod.jsonl
    

![DOD FILTER BY DATE](/assets/dod_filter_date.png)


As we can see from the photo of the CSV (We can use the _json2csv.py_ utility listed on the Visualization page and demonstrated [below](#visual) to check this utility and those following), the first tweet entries are from the DOD in order of time created. 
    

### _filter_users.py_
   
This one can be a little tricky if the input file doesn't have proper formatting. The input must be supplied as a list in a TXT or CSV file. It can contain:

&nbsp;&nbsp;&nbsp;;&nbsp;screen names  
&nbsp;&nbsp;&nbsp;;&nbsp;user ids  
&nbsp;&nbsp;&nbsp;;&nbsp;screen name,user id  
&nbsp;&nbsp;&nbsp;;&nbsp;user id,screen name  
   
each on a separate line.

We're going to use screen names for this example. We can collect these using _json2csv.py_.


![DOD FILTER BY USERS INPUT1](/assets/dod_filter_users_input1.png)


We can then copy the screen names (in this case, the first screen names listed) into our file of choice. 


![DOD FILTER BY USERS INPUT2](/assets/dod_filter_users_input2.png)


Once we run our usage command, we will get a JSON containing only the tweets made by the screen names we listed in the file. 

 
    python utils/filter_users.py nh_dod_sn.txt nh_dod.jsonl > nh_dod_users.jsonl
    

![DOD FILTER BY USER](/assets/dod_filter_users.png)


The output is the metadata about the users we supplied. Notice that there is no cap on the number of tweets by the same screen name.      
    
### _geo.py_ 


Before working with this utility, check out the [not_mapping_twitter repo](https://github.com/ucsb-collaboratory/not_mapping_twitter) to read the precautions of geocoordinates. 

Now we can create a file of tweets containing geo coordinates. 


    python utils/geo.py nh_dod.jsonl > nh_dod_geo.jsonl
    
    
![DOD GEO](/assets/dod_geo.png)


Based on our results, there are only two tweets in our sample dataset (after being filtered by DOD) that contain geo coordinates. 
    

### _geofilter.py_ 


_geofilter.py_ works similarly to _geo.py_, but allows us to specify whether we want to filter by absence OR presence of geo coordinates. By specifying that we want to filter by tweets without geo coordinates, we can get the tweets not returned by _geo.py_. 


    python utils/geofilter.py nh_dod.jsonl --no-coordinates > nh_dod_geofilter.jsonl
  

![DOD GEO FILTER](/assets/dod_geo_filter.png)

    
### _noretweets.py_


Next, we'll remove retweets from our dataset. 


    python utils/noretweets.py nh_dod.jsonl > nh_dod_noretweets.jsonl


### _sensitive.py_

This utility will allow us to filter by the presence or absense of sensitive content in tweets. 
    
    python utils/sensitive.py nh_dod.jsonl > nh_dod_sensitive.jsonl
    
    
Column R is the variable possibly_sensitive, a boolean value (TRUE or FALSE) representing whether the tweet is considered sensitive. This first image is the dataset before running the utility sensitive.py. 
    

![DOD NOT SENSITIVE](/assets/dod_notsensitive.png)


The tweet that had been identified as sensitive has now been removed. 


![DOD SENSITIVE](/assets/dod_sensitive.png)
    

### _search.py_

This utility enables us to search for specific keywords in the dataset. Tweets containing the keyword will be output to the output file. We'll search the dataset for tweets containing the word 'shot'.


    python utils/search.py shot nh_dod.jsonl > nh_dod_search.jsonl
    

![DOD SEARCH SHOT](/assets/dod_search.png)   


By searching shot, we can identify (for the most part) the tweets that are reacting to Nipsey Hussle getting shot. As you might notice, the first tweet returned is using 'shot' in a different context. 
    

<a name="extract"/>


## Extracting the Data

Data extraction utilities focus on extracting and returning specific tweet metadata.


### _embeds.py_

This utility creates a list of media urls used in the dataset. 


    python utils/embeds.py nh_dod.jsonl > nh_dod_embeds.txt
    

![DOD EMBEDS](/assets/dod_embeds.png)


### _emojis.py_   

We want to look at the emoji statistics i.e. which emojis are used and how often. 

    
    python utils/emojis.py nh_dod.jsonl > nh_dod_emojis.txt
    

![DOD EMOJIS](/assets/dod_emojis.png)
    

As we can see, there are 5 emojis that are the same symbol of different skin tones. The general sentiment of all emojis listed are representative of religion, grief, and sadness. 


### _extractor.py_

    python utils/extractor.py user:screen_name entities:hashtags -output nh_dod_extractor.csv


![DOD EXTRACTOR](/assets/dod_extractor1.png)   

![DOD EXTRACTOR](/assets/dod_extractor2.png)


### _flakey.py_

    twarc dehydrate nh_dod.jsonl > nh_dod_ids.txt


    python utils/flakey.py nh_dod_ids.txt > nh_dod_flakey.csv
     
  
![DOD FLAKEY](/assets/dod_flakey.png)


The output could also be a TXT.

    
### _media_urls.py_
    
    python utils/media_urls.py nh_dod.jsonl > nh_dod_media_urls.txt
    
![DOD MEDIA URLS](/assets/dod_media_urls.png)
    

### _retweets.py_
    
    python utils/retweets.py nh_dod.jsonl > nh_dod_retweets.jsonl
    
    
This returns a blank JSON because there are no retweets in the subsetted dataset filtered by date. However, when we run this on the original subsetted dataset:

    
    python utils/retweets.py nh_dod_tweets.jsonl > nh_dod_retweets.jsonl
    

![DOD RETWEETS](/assets/dod_retweets.png)


### _tags.py_
    
    python utils/tags.py nh_dod.jsonl > nh_dod_hashtags.txt
    

![DOD TAGS](/assets/dod_tags.png)
    

### _times.py_
    
    python utils/times.py nh_dod.jsonl > nh_dod_times.txt
    

![DOD TIMES](/assets/dod_times.png)
    

### _tweets.py_
  
    python utils/tweets.py nh_dod.jsonl > nh_dod_tweets.txt
    
![DOD TIMES](/assets/dod_tweets.png) 


*Needs updated ability to handle tweets that have text labeled as "full_text" rather than "text".*

    
### _tweetometer.py_
 
    python utils/tweetometer.py nh_dod.jsonl > nh_dod_tweetometer.csv
    
![DOD TWEETOMETER](/assets/dod_tweetometer.png)
    
### _tweet_text.py_
    
    python utils/tweet_text.py nh_dod.jsonl > nh_dod_tweet_text.txt
    
![DOD TWEET TEXT](/assets/dod_tweet_text.png)
    
### _tweet_urls.py_
    
    python utils/tweet_urls.py nh_dod.jsonl > nh_dod_tweet_urls.txt
    
![DOD TWEET TEXT](/assets/dod_tweet_urls.png)
    
### _users.py_
    
    python utils/users.py nh_dod.jsonl > nh_dod_users.txt
    
 ![DOD TWEET TEXT](/assets/dod_users.png)   

<a name="visual"/>

## Visualizing the Data

This section allows us to create visuals of the data. 

### _geojson.py_

We can use geojson.py to create a GeoJSON file when the geospatial location of a tweet is available.  


    python utils/geojson.py nh_dod.jsonl > nh_dod.geojson 
    
We can then use a [GeoSpatial JSON reader](http://geojsonviewer.nsspot.net/) to visualize this file on the map.  
    
![DOD GEOJSON](/assets/dod_geojson.png)

We can do further manipulation by creating a centroid instead of a bounding box.

    python utils/geojson.py --centroid nh_dod.jsonl > nh_dod_centroid.geojson
    
![DOD CENTROID GEOJSON](/assets/dod_centroid.png)

Or we can add a random lon and lat shift to the bounding box centroids (0-0.1)

    python utils/geojson.py --centroid --fuzz 0.01 nh_dod.jsonl > nh_dod_fuzz.geojson
    
![DOD FUZZ GEOJSON](/assets/dod_fuzz.png)

As we can see below, the shift is not too big.

![DOD CENTROID VS FUZZ GEOJSON](/assets/dod_centroidvsjson.png)
    
*Jon's tidbit about mapping Twitter*
   
### _json2csv.py_

We can view the tweets in a more cohesive manner by turning our json into a csv. 

*Note: if you're using Windows and you get a charmap error, you can change your Region settings using the instructions [here](https://scholarslab.github.io/learn-twarc/08-win-region-settings)*

    python utils/json2csv.py nh_dod.jsonl > nh_dod_tweets.csv
    
 ![DOD CSV](/assets/dod_json2csv.png)
    
### _network.py_

    python utils/network.py nh_dod.jsonl nh_dod_network.html
    
![DOD NETWORK](/assets/dod_network.png)

We can click on the dots to see the individual tweets. The central node(red) is the original tweet of a video interview. The connected nodes(yellow) are the replies and retweets to/of that video. The other nodes(gray) are attached by similarity to that central node and it's surrounding nodes. 

![DOD NETWORK VIDEO](/assets/dod_network_video.gif)

We can move the cluster by clicking on one of the nodes and dragging it to the place on our screen we would like it to be. The bigger the data size, the longer it will take to mode the nodes around. There are also nodes not attached to the cluster. 

### _source.py_

We can create a page with the sources(ranked most to least) used with source.py.

    python utils/source.py nh_dod.jsonl > nh_dod_source.html
    
*Note: The html is hardcoded in the source.py file. The title of the page is set to 'Title Here'. To change this, you have to edit the html code itself from ['Title Here'](https://github.com/DocNow/twarc/blob/3dd763516e643d070fab237bd5fb18b1274ec738/utils/wall.py#L113) to the title of your choice*  
    
   
![DOD SOURCE](/assets/dod_source.png)


We can click on the links provided for each source to learn more about them. 
  

### _wall.py_

We can also create a wall of tweets. 

    python utils/wall.py nh_dod.jsonl > nh_dod_wall.html
    

![DOD WALL](/assets/dod_wall.png)
   

### _wordcloud.py_    

The last visualization tool we'll go over is creating a wordcloud. 
    
    python utils/wordcloud.py nh_dod.jsonl > nh_dod_wordcloud.html
    

![DOD WORDCLOUD](/assets/dod_wordcloud.png)


<a name="status"/>

## Getting the Status the Data

    
### _deleted_users.py    

We can run deleted_users.py to produce a JSON containing the tweets that have been deleted. 
    
    python utils/deleted_users.py nh_dod.jsonl > nh_dod_deleted_users.jsonl
   
   
![DOD DELETED USERS](/assets/dod_deleted_users.png)
   
   
### _deletes.py_    

We can then feed the output JSON into deletes.py to see the reason the tweet has been deleted. 
    
    python utils/deletes.py nh_dod_deleted_users.jsonl > nh_dod_deletes.txt
    
    
![DOD DELETES](/assets/dod_deletes.png)


### _foaf.py_ 
   
    python utils/foaf.py 2267720350
    
%Just trying to figure out how to open the SQL file%

### _oembeds.py_
    
    python utils/oembeds.py nh_dod.jsonl > nh_dod_oembeds.jsonl
    
*Note: Warning messages like the following will be printed to the command line if the url has been deleted.*     
    
 
![DOD OEMBEDS WARNING](/assets/dod_oembeds_warning.png)

    
### _tweet.py_

We'll use one of the first tweet id in our dataset. 
    
![DOD TWEET ID](/assets/dod_tweet_id.png)
    
    python utils/tweet.py 1112143431197835264 > dod_tweet.jsonl

 
### _tweet_compliance.py_
    
    python utils/tweet_compliance.py nh_dod_ids.txt > nh_dod.jsonl > nh_dod_tweet_compliance.jsonl
    
The current tweets will be output to a dod_tweet_compliance.jsonl.
    
![DOD TWEET COMPLIANCE](/assets/dod_tweet_compliance.png)

The ids of tweets that are not available are output to the command line along with the deleted tweets. 


![DOD TWEET COMPLIANCE](/assets/dod_tweet_compliance1.png)

    
### _wayback.py_

    
    python utils/wayback.py nh_dod.jsonl > dod_wayback.txt
    

![DOD WAYBACK](/assets/dod_wayback.png)


<a name="organize"/>


## Organizing the Data


### _sort_by_id.py_

This one is pretty simple. It just sorts the dataset in ascending order by id. It's essentially the same as sorting by date as tweet ids are parsed out in order of creation.

    python utils/sort_by_id.py nh_dod.jsonl > nh_dod_sort_by_id.jsonl
    
 
[Back To Top](#worked-example)

