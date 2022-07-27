'''First, ask the user how many numbers he/she wants to enter. Once we have the number, find the min,max,avg,sum of those numbers'''

target = int(input('Enter the number of digits you want to enter: '))

emptlist = []
t = 1
for i in range(0,target):
    inpt = int(input('Enter the digit {}: '.format(t)))
    emptlist.append(inpt)
    t += 1

print('\n',emptlist)

print('\nFinding the min,max,avg,sum of the list\n')

print('minimum value: ',min(emptlist))
print('maximum value: ',max(emptlist))
print('average value: ',sum(emptlist)/len(emptlist))
print('sum: ',sum(emptlist))