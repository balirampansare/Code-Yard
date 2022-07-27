'''Take 2 digits from the user as input and swap the values of those two variables'''

#------------------------METHOD 1---------------------#
var1 = int(input('Enter the value for variable 1: '))
var2 = int(input('Enter the value for variable 2: ')) 

print('\nSwapping the values of variables using METHOD 1')
print('Before Swapping:',var1,var2)
temp = var1
var1 = var2
var2 = temp

print('After swapping:',var1,var2)


#------------------------METHOD 2---------------------#

print('\nSwapping the values of variables using METHOD 2')
print('Before Swapping:',var1,var2)
var1,var2 = var2,var1
print('After swapping:',var1,var2)


#------------------------METHOD 3---------------------#

print('\n5Swapping the values of variables using METHOD 3')
print('Before Swapping:',var1,var2)
var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print('After swapping:',var1,var2)