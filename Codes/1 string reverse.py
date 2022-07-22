'''
reversing the string using first function is using slice reverse and the second fuction is of reversing the stirng using for loop
Shown with two methods
'''

#-------------------------------------CODE-----------------------------------------#

#METHOD - 1#
def slice_reverse(text):
    reverse1 = text[::-1]
    print(reverse1)

#METHOD - 2#
def for_reverse(text):
    rev_text = ""
    for i in text:
        rev_text = i + rev_text #concatenate 
    print(rev_text)
    
text = 'hello'
slice_reverse(text)
for_reverse(text)