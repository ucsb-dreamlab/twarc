---
date: 03/02/2021
output: html
---

##### Table of Contents  
[deduplicate.py](#headers)  
[filter_date.py](#filter_date.py)  
[filter_users.py](#filter_users.py )  
[gender.py](#gender.py)  
[geo.py](#geo.py)  
[geofilter.py](#geofilter.py) 
[noretweets.py](#noretweets.py) 
[sensitive.py](#sensitive.py)  
[search.py](#search.py)  
[twarc-archive.py](#twarc-archive.py) 
[webarchives.py](#webarchives.py) 


<a name="headers"/>
 
## deduplicate.py
This utility removes tweets with duplicate IDs. According to the Twitter documentation, duplicate tweet ids are possible for tweets collected from the Twitter filter stream. 

Usage:

    python utils/deduplicate.py tweets.jsonl > deduped.jsonl
    
Arguments: 

    --extract-retweets 
    
For help: 

    python utils/deduplicate.py -h 
    
Output is a JSON containing the data without duplicate ids (i.e. the same tweet). Specification of an output file is not necessary, however, without specification, output will be printed to the cmd.  


## filter_date.py
filters tweets by date supplied

## filter_users.py 
filters tweets by user

## gender.py 
filters tweets by gender

## geo.py 
filters tweets by presence or absence of geo coordinates

## geofilter.py 
filters tweets by presence or absence of geo coordinates

## noretweets.py
filters out retweets from tweets 

## sensitive.py 
filters tweets by presence or absence of possibly sensitive content

## search.py 
filters tweets by regular expression given

## twarc-archive.py 
filters tweets by specific word supplied

## webarchives.py 
filters tweets by presence or absence of webarchive
