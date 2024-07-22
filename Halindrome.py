#wipro question
'''
Question: count Halindromes of given strings
conditions:
1.string itself should be palidrome then
 count+=1
 or
2.if not palindrom then
  divide string in two parts
  if the string is even length, divide half
  if the string is odd length (5) divide as 3 and 2
  if there is atleast one part of the string is palindrom
  count+=1 and that string is said to be a HALINDROME
  else NOT A HALINDROME
INPUT  
s=['aba','sasdad','aaaccc','tapdog','emepe']
OUTPUT
count=3

'''
import math

def palindrome(word):
    length=len(word)
    for i in range(0,length):
        rev=word[::-1]
        if word==rev:
            return rev
        else:
            return ''

  

s=['aba','sasdad','aaaccc','tapdog','emepe']
count=0
for i in s:
    string=i
    reverse=palindrome(string)
    if(string==reverse):
        count+=1
        print(string,'->palindrome')
    else:
        mid=math.ceil(len(string)/2)
        first_str=string[0:mid]
        second_str=string[mid:]
        print(first_str,end=' ')
        print(second_str,end=' ')
        print()
        first_reverse=palindrome(first_str)
        second_reverse=palindrome(second_str)

        if(first_str==first_reverse or second_str==second_reverse):
            count+=1
            print(string,'->Halindrome')
        else:
            print(string,'->not a Halindrome')
            
    print()     
print('No. of strigs that are Halindrome are',count)
