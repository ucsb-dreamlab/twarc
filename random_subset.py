'''
This python program will take a file of dehydrated tweets and n random tweets ids where n is the user's chosen subset length. To use this program, download it from Github and store it in your twarc utilities file. 

Usage: python utils/random_subset.py 

Takes user input of the following:

tweets - The name of the original tweet id file you'd like to take a subset of. This should be entered without quotes. Example user input: nh_ids.txt
subset - The name of a file you would like the subset ids to output to. The file doesn't have to exist prior as it will be created. Example user input: nh_sub_tweets.txt
length - The length you'd like your subset to be. Example user input: 20000
total - The total number of tweet ids in the dataset you'd like to take a subset of. 

Each id must be on a separate line in the original tweet file for this to work. The program reads line by line. 
'''

import random

'''  User Input  '''
# change to allow parsers like they use in the utilities
tweets = input("Enter the name of your tweet id file: ")
subset = input("Enter the name of the output tweet id file: ")
length = int(input("Enter the number of tweet ids you would like to subset: "))
total = int(input("Enter the total number of tweet ids in the dataset: "))


'''  Generating Random Line Numbers  '''
print("Generating random ids...")
rand_lines = [] # create an empty list to hold the random line numbers
num_lines = 0 # create a counter to track the number of lines

while num_lines < length: # while the number of lines is less than the subset length
    num = random.randrange(total)# create a random line number 
    if num not in rand_lines: # if the number isn't already in the list 
        rand_lines.append(num) # add it
        num_lines += 1 # increase the counter

'''  Reading Files; Writing Random Tweet Ids To New File  '''
with open(tweets, 'r') as firstfile, open(subset, 'a') as secondfile: # open both files
        print("Transfering random ids...")
        count = 0 # number of lines in interation
        for i, line in enumerate(firstfile):
                if count == length: # stop if length of subset has been reached
                        break
                elif i not in rand_lines: # if the line number is not in the list of random lines
                        continue
                else: # if it isn't, add it
                        secondfile.write(line) # writing to the file
                        count += 1 # increasing the counter
                        
'''  Close Both Files  '''
firstfile.close()
secondfile.close()

print("Finished loading {} ids".format(count))
