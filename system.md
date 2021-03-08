---
date: 03/08/2021
output: html
---

##### Table of Contents  
[auth_timing.py](#headers)  
[remove_limit.py](#remove_limit.py)  
[validate.py](#validate.py)  

<a name="headers"/>

## auth_timing.py
This utility allows search 450 requests every 15 minutes, and User Auth contexts at 180 requests per 15 minutes. It exercises both and counts how many tweets it’s able to receive.

Usage:

    Usage: python utils/auth_timing.py tweets.jsonl 

## remove_limit.py
This utility removes limit warnings from filter API.

Usage: 

    python utils/remove_limit.py tweets.jsonl > tweets_no_warnings.jsonl
    
## validate.py
This utility removes unused imports.

Usage: 

    python utils/validate.py election.json
    
Output only returned if JSON import is invalid.

