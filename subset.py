'''

We would like to take a subset of 20000 Nispey Hussle tweet ids listed on
separate lines in the txt file nh_ids.txt and transfer them to a new file
nh_sub_ids.txt for rehydration

'''

# open both files
with open('nh_ids.txt', 'r') as firstfile, open('nh_sub_ids.txt', 'a') as secondfile:
        # set i as the number of tweet ids you would like to transfer
        for i, line in enumerate(firstfile):
                if i == 20000:
                        # if the number of lines is 20000, break
                        break
                else:
                        # if it isn't keep adding
                        secondfile.write(line)
                

firstfile.close()
secondfile.close()

