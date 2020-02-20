
from collections import Counter

inp = list(input('inp: ')) 
print()
# input the text to be encoded

chars = Counter(inp).most_common().reverse()
# creates an array in order of occurance (lowest to highest)
# stores as an array of tuples: ('character', frequency)

print('chars:', chars)
print()
# prints out the dict 'chars' - debug
