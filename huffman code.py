    '''
    note to mgrove36:
    please read throught the code and comments, ant see if everything is working as
    planned (i.e. as the comments explain)
    if not, please tell me which ones and can we have a look together?
    alos, i dont think the while loop works yet
    '''

from collections import Counter

inp = list(input('inp: ')) 
print('')
# input the text to be encoded

chars = {} 
# creating a dictionary 'chars'


sort_inp = [item for items, c in Counter(inp).most_common() for item in [items] * c] 
# sorts the items in the list 'inp' in order of occurence

print('sort_inp:', sort_inp)
print('')
# prints out the sorted list - debug

for i in sort_inp:
    if i in chars:
        chars[i] += 1
    else:
        chars[i] = 1
# adds each character, with its frequency to the dict 'chars'

print('chars:', chars)
print('')
# prints out the dict 'chars' - debug

char_list = list(chars)
char_list.reverse()
# changes the dict 'chars' into the list 'char_list', in the opposite order
# this means that the items will be in acsending order

print('char_list:', char_list)
print('')
# prints the list 'char_list' - debug

left_val = []
right_val = []
# creates lists for the left and right values


half_list = int(len(char_list)/2)
# sets variable 'half_list' to half the length of the list
# also makes sure that 'half_list' is an integer, not a float

print('half_list:', half_list)
print('')
# prints variable 'half_list' - debug

huffmaned = False 
n = -1
# creats variables for the while loop


while not huffmaned:
    n += 1
    temp = []

    try:
        for i in range(half_list)
            k =  i + n
            temp.append(char_list[k])
        # selects which characters go on which side of the tree
        # it does this by using the variable 'n', when n is less than half of the length of the list,
        # the for loop sets temp to the odd values, and visa versa 

    except:
        break
    # if any of the values ('k'/'n') are out of range, it moves on

    print('temp:', temp)
    print('')
    # prints list 'temp' - debug

    if n < half_list:
        right_val.append(temp)
    # puts 'temp' into 'right_val' if the try-except statement is getting the values for the 
    # right side of the tree
 
    elif n > half_list:
        left_val.append(temp)
    # puts 'temp' into 'left_val' if the try-except statement is getting the values for 
    # the left side of the tree

    # these work as n has to be greater than half the length of the list to get the values for
    # the left side, and less for the right side



    
'''
to do:
separate the right and left sides of the tree
make the loop work for larger lists
add the comments when finished    
'''

print('right_val:', right_val)
print('')
# prints the list 'right_val' - debug

print('left_val:', left_val)
print('')
# prints the list 'left_val' - debug

tree = []
# creates list 'tree' for the final tree

tree.append(left_val)
tree.append(right_val)
# adds the lists 'left_val' and 'right_val' to the list 'tree'

print(tree)
print('')
#prints the list 'tree' - debug