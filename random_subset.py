import random

tweets = input("Enter the name of your tweet json: ")
subset = input("Enter the name of the output json: ")
length = int(input("Enter the number of tweets you would like to subset: "))

# create an empty list to hold the random line numbers
rand_lines = [0]
# set count to 0
count = 0
for count in range(length+1): # iterate until it reaches subset length
    num = random.randrange(1,length) # call the random function to generate
    if num not in rand_lines: # make sure we don't have duplicate lines
        rand_lines.append(num)
    count += 1
print(rand_lines)


# open both files
with open(tweets, 'r') as firstfile, open(subset, 'a') as secondfile:
        counter = 0
        # set i as the number of tweet ids you would like to transfer
        for i, line in enumerate(firstfile):
                if counter == length:
                        # if the number of lines is 20000
                        break
                elif i not in rand_lines:
                        continue
                else:
                        # if it isn't keep adding
                        secondfile.write(line)
                        counter += 1
                        print(counter)

firstfile.close()
secondfile.close()
