---
date: 03/15/2021
output: html
---
[Utilities Home](utilities.md) • [Filtering](filtering.md) • [Extraction](extraction.md) • [Visualization](visualization.md) • [Status](status.md) • [Organization](organization.md) • [System](system.md)

# Worked Example

For the worked example, we will run through the [2019 Nipsey Hussle Funeral Tweets](https://archive.org/details/nipsey-hustle-tweets). The tweet ids are available under Downloadable Options on the right-hand side of the page and are named nipsey-ids.txt.gz. (Note: The extension .gz is a file format and software application used for file compression and decompression. If you don't know how to open this type of file or are having trouble doing so, visit Utilities Home and scroll to Resources). 

If you have not downloaded Twarc, do so at the [Twarc Doc Now](https://github.com/DocNow/twarc). For a more non-technical-user download, visit [scholarslab](https://scholarslab.github.io/learn-twarc/06-twarc-command-basics.html). Once Twarc is downloaded, be sure to start the twarc session. 

You are encouraged, but not required, to try out these utilities on your own before viewing the worked example code and outputs. 

##### Table of Contents  
[Prepping the Data](#prep)  

  
<a name="prep"/>

## Prepping the Data

The first step will be to unzip out dataset. It should unzip to a txt file titled ids.txt. For organizational purposes, we will rename this file nh_ids.txt for Nispey Hussle. You can keep the name ids.txt or modify it to fit your needs.

There are 11,642,103 ids listed in ids.txt. This amount of data is normally great for analysis because it gives us so much to work with. However, it also takes a long time to process. For this example, we will only be looking at the first 20,000 tweets. For ease of use, I have written the python code to do this. Click 'View on Github' at the top of this page or visit the [ucsb-collaboratory twarc repository](https://github.com/ucsb-collaboratory/twarc) to download the file subset.py. Once downloaded, simply run subset.py to appy it to your ids file. You can alter the length of the subset by changing the variable x. The outputted file is titled nh_sub_ids.txt. 

Then we will need to rehydrate the dataset. This can be done using the following command:

    twarc hydrate nh_sub_ids.txt > nh__sub_tweets.jsonl
    
*Note: If an account or tweet has been deleted from Twitter, it cannot be rehydrated. We will discuss this more later on*


