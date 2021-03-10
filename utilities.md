---
date: 03/02/2021
output: html
---
# Twarc Utilities

##### Table of Contents  
[Filtering](#headers)  
[Extraction](#extraction)  
[Visualization](#visualization)  
[Status](#status)  
[Organization](#organization)  
[System](#system) 
[Extra Resources](#extraresources) 

Here are the python utilities accessible with twarc. Every section (except for Extra Resources) links to a new page containing the python utilities listed below it. These pages can be accessed by clicking on the blue headings below. 
  
<a name="headers"/>

## [Filtering](filtering.md)
  - deduplicate.py: filters out duplicate ids from tweets
  - filter_date.py: filters tweets by date supplied
  - filter_users.py: filters tweets by user
  - gender.py: filters tweets by gender
  - geo.py: filters tweets by presence or absence of geo coordinates
  - geofilter.py: filters tweets by presence or absence of geo coordinates
  - noretweets.py: filters out retweets from tweets 
  - sensitive.py: filters tweets by presence or absence of possibly sensitive content
  - search.py: filters tweets by regular expression given
  - twarc-archive.py: filters tweets by specific word supplied
  - webarchives.py: filters tweets by presence or absence of webarchive

## [Extraction](extraction.md)
  - embeds.py: extracts list of media urls
  - emojis.py: extracts emojis and number of times used
  - extractor.py: overall extractor of attributes
  - flakey.py: extracts creation times for snowflake ids
  - media_urls.py: extracts id and url of images
  - media2warc.py: saves media to warc 
  - retweets.py: extracts original tweet id and number of times retweeted
  - tags.py: extracts hashtags and number of times used
  - times.py: extracts times tweets were made
  - tweets.py: extracts id, time, tweet text,...
  - tweetometer.py: extracts supplied tweet attributes to csv
  - tweet_text.py: extracts username and full text
  - tweet_urls.py: extracts urls
  - users.py: extracts user names/screen names

## [Visualization](visualization.md)
  - geojson.py: creates a geojson file that can be used for geo visualization
  - json2csv.py: creates a csv of tweets
  - network.py: creates a static D3 network of tweets
  - source.py: creates a page of which twitter client sources are msot used
  - wall.py: creates a wall of tweets
  - wordcloud.py: creates a wordcloud of tweets

## [Status](status.md)
  - deleted.py: checks the status of each tweet, outputting tweets that have been deleted
  - deletes.py: takes deleted tweet output and determines why tweet/user was deleted
  - deleted_users.py: checks the status of each tweet, outputting tweets/users that have been deleted
  - foaf.py: finds the friend of a friend network for a particular user	
  - oembeds.py: reads a stream of tweet JSON and augments .entities.urls with oembed metadata for the URL
  - tweet.py: fetches tweet from twitter stream using tweet id, if it exists
  - tweet_compliance.py: provides most recent version of a tweet, if it exists
  - wayback.py: reads stream of tweets and checks whether that tweet is archived at Internet Archive

## [Organization](organization.md)
  - sort_by_id.py: sorts tweets by id
  - unshrtn.py: unshortens urls 
  - urls.py: takes unshorted urls and prints them out
  - youtubedl.py: uses youtube-dl to download video content in tweets
 
## [System](system.md)
  - auth_timing.py: allows search 450 requests every 15 minutes, and User Auth contexts at 180 requests per 15 minutes
  - remove_limit.py: removes limit warnings from API
  - validate.py: removes unused imports

## [Worked Example](workedex.md)
  - Here you'll find a worked example of all the utilities listed above. 

## Extra Resources
  - For Twarc Setup and basics click [here](https://scholarslab.github.io/learn-twarc/06-twarc-command-basics.html) and/or [here](https://github.com/DocNow/twarc)
  - MAC terminal command [cheat sheet](https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/) 
  - Windows command prompt [cheat sheet](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf)
  - Windows powershell can be found in the microsoft store for free. [This](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) is a good resource on powershell and why you might want to download it. 
  - Linux command line [cheat sheet](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)
  - JSON Chrome viewer [extension](https://chrome.google.com/webstore/detail/json-viewer/aimiinbnnkboelefkjlenlgimcabobli?hl=en-US)
