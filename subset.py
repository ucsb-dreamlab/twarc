'''
Takes user input of the following:

tweets - The name of the original tweet id file you'd like to take a subset of. This should be entered without quotes. Example user input: nh_ids.txt
subset - The name of a file you would like the subset ids to output to. The file doesn't have to exist prior as it will be created. Example user input: nh_sub_tweets.txt
length - The length you'd like your subset to be. Example user input: 20000

Each id must be on a separate line in the original tweet file for this to work. The program reads line by line. 
'''

tweets = input("Enter the name of your tweet json: ")
subset = input("Enter the name of the output json: ")
length = int(input("Enter the number of tweets you would like to subset: "))

# open both files
with open(tweets, 'r') as firstfile, open(subset, 'a') as secondfile:
        # set i as the number of tweet ids you would like to transfer
        for i, line in enumerate(firstfile):
                if i == length:
                        # if the number of lines is 20000, break
                        break
                else:
                        # if it isn't keep adding
                        secondfile.write(line)

firstfile.close()
secondfile.close()

