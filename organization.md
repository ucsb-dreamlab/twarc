---
date: 03/08/2021
output: html
---
[Utilities Home](utilities.md) • [Filtering](filtering.md) • [Extraction](extraction.md) • [Visualization](visualization.md) • [Status](status.md) • Organization • [System](system.md) • [Worked Example](workedex.md) • [Resources](resources.md)


# Organization Utilities

##### Table of Contents  
[sort_by_id.py](#sort_by_id.py)  
[unshrtn.py](#unshrtn.py)  
[urls.py](#urls.py)  
[youtubedl.py](#youtubedl.py)  

<a name="sort_by_id.py"/>

## sort_by_id.py
This utility sorts tweet ids into chronological ascending order(i.e. sorting tweets by creation date). 

Usage: 

    python utils/sort_by_id.py tweets.jsonl > sort_by_id.jsonl

<a name="unshrtn.py"/>

## unshrtn.py
This utility unshortens urls. The microservice _unshrtn_ is needed to run this utility. [unshrtn](https://github.com/DocNow/unshrtn) best run with Docker [Docker](https://www.docker.com/get-started).

Usage: 

    cat tweets.jsonl | utils/unshrtn.py > unshortn.jsonl
    
Arguments: 

    --pool-size POOL_SIZE (number of urls to look up in parallel)
    --unshrtn UNSHRTN  (url of the unshrtn service)
    --retries RETRIES  (number of time to retry if error from unshrtn service)
    --wait WAIT         (number of seconds to wait between retries if error from unshrtn service)

For help: 

    python utils/unshrtn.py -h

<a name="urls.py"/>

## urls.py
This utility takes the unshortened JSON and prints out each url.

Usage: 

    cat unshortn.jsonl | utils/urls.py | sort | uniq -c | sort -nr > urls.txt

<a name="youtubedl.py"/>

## youtubedl.py
This utility downloads video content referenced in tweet data, from over a thousand video providers. It also downloads JSON metadata for each video, and the transcript if one is available.

The command line program _youtube-dl_ is needed to run this utility. youtube-dl is detailed [here](https://github.com/ytdl-org/youtube-dl). 

Usage: 

    python utils/youtubedl.py election.json
    
Arguments: 

    --max-downloads MAX_DOWNLOADS (max downloads per URL)
    --max-filesize MAX_FILESIZE (max filesize to download in bytes)
    --ignore-livestreams (ignore livestreams which may never end)
    --download-dir DOWNLOAD_DIR (directory to download to)
    --block BLOCK (hostnames to block (repeatable)
    --timeout TIMEOUT (timeout download after n seconds)
    
For help: 

    python utils/youtubedl.py -h

[Back To Top](#organization-utilities)
