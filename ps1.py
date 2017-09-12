###### this is the first .py file ###########

####### write your code here ##########
from collections import Counter

n = raw_input()    #take the input of bit stream

list1 = list(n)     #convert it into list

noOfones = list1.count('1')

rem = noOfones%2

if(rem==0):
	list1.append('1')

else:
	list1.append('0')
	
ubit = ''.join(list1)
print  ubit  #print the bit data with parity bit

#bit stuffing.......

sub = '010'

# To find the sub string into given string

def find_substring(string,sub_string):
	   # str1 = string 
	    for i in range(len(string)):
		if(string[i]==sub_string[0]):
		  
		    flag = string.find(sub_string, i, i+len(sub_string))
		    if(flag>=0):
		 	string = string[:i+len(sub_string)]+'0'+string[i+len(sub_string):] 
	    return string


ustr = find_substring(ubit,sub)

lbits = ustr[len(ustr)-2:len(ustr)]

if(lbits=='01'):
	ustr = ustr+'0'

#print lbits
# final modified string received at the other end
print ustr+'0101'



