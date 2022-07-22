'''
1. from the string print out all the distinct charachter of the string along with their count of the distinct charachter appeared in the string.
2. you will be given one target word check out how many time the word has been occured in the string.
'''

'''
string = "I can give is bye-bye"
target = bye

Required Output:
{'I': 1, ' ': 5, 'c': 1, 'a': 1, 'n': 1, 'g': 1, 'i': 2, 'v': 1, 'e': 3, 's': 1, 'b': 2, 'y': 2}
the target "bye" is appeared in the string for 2 times

'''
#------------------------------------------------------CODE-------------------------------------------------#

string1 = 'I can give is bye bye'

dict = {}
for i in string1:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

target = 'bye'

count = 0
wrd = string1.split(' ')
for i in range(len(wrd)):
    if wrd[i] == target:
        count += 1
print('the target "{0}" is appeared in the string for {1} times'.format(target,count))