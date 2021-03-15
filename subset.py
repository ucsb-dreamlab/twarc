'''

We would like to take a subset of 20000 Nispey Hussle tweet ids listed on
separate lines in the txt file nh_ids.txt and transfer them to a new file
nh_sub_ids.txt for rehydration

'''

# open both files
with open('nh_ids.txt', 'r') as firstfile, open('nh_sub_ids.txt', 'a') as secondfile:
    # set the variable x as the number of tweet ids you would like to transfer
    x = 20000
    # use a for loop to get every line in the file
    for line in firstfile:
        # use a while loop to limit the number of lines 
        while x != 0:
            # append content to second file
            secondfile.write(line)
            # update count variable
            x -= 1


