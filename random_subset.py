import random

'''  User Input  '''
tweets = input("Enter the name of your tweet id file: ")
subset = input("Enter the name of the output tweet id file: ")
length = int(input("Enter the number of tweet ids you would like to subset: "))
total = int(input("Enter the total number of tweet ids in the dataset: "))


'''  Generating Random Line Numbers  '''
rand_lines = [] # create an empty list to hold the random line numbers
num_lines = 0 # create a counter to track the number of lines

while num_lines < length: # while the number of lines is less than the subset length
    num = random.randrange(total)# create a random line number 
    if num not in rand_lines: # if the number isn't already in the list 
        rand_lines.append(num) # add it
        num_lines += 1 # increase the counter

print(len(rand_lines)==length) # check the length of the list is equal to the subset


'''  Reading Files; Writing Random Tweet Ids To New File  '''
with open(tweets, 'r') as firstfile, open(subset, 'a') as secondfile: # open both files
        count = 0 # number of lines in interation
        for i, line in enumerate(firstfile):
                if count == length: # stop if length of subset has been reached
                        break
                elif i not in rand_lines: # if the line number is not in the list of random lines
                        continue
                else: # if it isn't, add it
                        secondfile.write(line) # writing to the file
                        count += 1 # increasing the counter
                        print(count)

'''  Close Both Files  '''
firstfile.close()
secondfile.close()

