---
date: 03/08/2021
output: html
---
[Utilities Home](utilities.md) • [Filtering](filtering.md) • [Extraction](extraction.md) • [Status](status.md) • [Organization](organization.md) • [System](system.md) • [Worked Example](workedex.md)


# Visualization Utilities

##### Table of Contents  
[geojson.py](#geojson.py)  
[json2csv.py](#json2csv.py)  
[network.py](#network.py)  
[source.py](#source.py)  
[wall.py](#wall.py)  
[wordcloud.py](#wordcloud.py) 

<a name="geojson.py"/>

## geojson.py
This utility outputs a GeoJSON file when geo spatial location is available containing the following attributes:
- Twitter user name
- Twitter user screenname
- Tweet creation time
- Tweet status text
- Profile image url
- The tweet url

Usage: 

    python utils/geojson.py tweets.jsonl > tweets.geojson
    
Arguments:  

    -c, --centroid (store centroid instead of a bounding box)
    -f FUZZ, --fuzz FUZZ (add a random lon and lat shift to bounding box centroids (0-0.1))
    
For help:  

    python utils/geojson.py -h

The best way to visualize what this is doing, is to use a geojson chrome extension or [geojson reader](https://chrome.google.com/webstore/detail/geojson-map-viewer-with-d/hcfcnnifdgkogkjjlkpdcfalegleggdg?hl=en-US). 

<a name="json2csv.py"/>

## json2csv.py
This utility converts a json to a csv to be easily read.

Usage: 

    python utils/json2csv.py tweets.jsonl > tweets.csv
    
Arguments:   

    --output OUTPUT, -o OUTPUT (write output to file instead of stdout)
    --split SPLIT, -s SPLIT (if writing to file, split into multiple files with this many lines per file)
    --extra-field EXTRA_FIELD EXTRA_FIELD, -e EXTRA_FIELD EXTRA_FIELD (extra fields to include. Provide a field name and a pointer to the field. Ex: -e verified  user.verified)
    --excel, -x  (create file compatible with Excel)

For help: 

    python utils/json2csv.py -h

<a name="network.py"/>

## network.py
This utility creates a network of tweets : static D3 visualization

Usage: 

    python utils/network.py tweets.jsonl network.html
    
It’s important to note that network.py commands do not use ‘>’ to signify an output file. With ‘>’, the file input and output will not be recognized.

Arguments: 

    --retweets (include retweets)
    --min_subgraph_size = MIN_SUBGRAPH_SIZE (remove any subgraphs with a size smaller than this number)
    --max_subgraph_size = MAX_SUBGRAPH_SIZE (remove any subgraph with a size larger than this number)
    --users(show user relations instead of tweet relations)
    --hashtags (show hashtag relations instead of tweet relations)

For help: 

    python utils/network.py -h
    
<a name="source.py"/>
    
## source.py
This utility creates a list of client sources most used and outputs a list with each source and the corresponding number of times it was used. 

Usage: 

    python utils/source.py tweets.jsonl > sources.html

<a name="wall.py"/>

## wall.py
This utility creates a rudimentary wall of tweets.

Usage: 

    python utils/wall.py tweets.jsonl > wall.html
		
To put the tweets on the wall in chronological order: 

    % tail -r tweets.jsonl | ./wall.py > wall.html 

<a name="wordcloud.py"/>

## wordcloud.py
This utility creates a wordcloud of the tweets, accounting for stop words (i.e. “and”, “the”, “to”, etc.). 

Usage: 

    python utils/wordcloud.py tweets.jsonl > wordcloud.html


[Back To Top](#visualization-utilities)
