
from collections import Counter
# imports function 'Counter' for later use

def find_nodes(nodes, target_character):
    # Function to find the path (to assign the binary value)
    # of a desired character

    for index, item in enumerate(nodes):
        # goes through the list 'nodes' and get the item and index as it does
        
        if item == target_character:
            return[str(index)]
            # if the item is the desired character it returns the path
        if isinstance(item, (list, tuple)):
            # runs this function again to go further into the nested items
            path = find_nodes(item, target_character)
            # if the desired character is found, this returns its path
            if path:
                return[str(index)] + path
                # if the desired character is not found, it returns an empt list
    return []

def tree_making():
    # function to create a huffman tree (and dictionary) for some text

    inp = list(input('inp: ')) 
    print()
    # input the text to be encoded

    chars = Counter(inp).most_common()
    chars.reverse()
    # creates an array in order of occurance (lowest to highest)
    # stores as an array of tuples: ('character', frequency)

    print(f'chars: {chars}')
    print()
    # prints out the list 'chars' - debug

    nodes = []
    freqs = []
    # defining lists 'nodes' and 'freqs' ...

    for item in chars:
        nodes.append(item[0])
        freqs.append(item[1])
    # sorts the list 'chars' into the lists 'nodes and 'freqs'

    while len(nodes) > 2:
        new_node = (nodes[0], nodes[1])
        # adds the first two items in 'nodes' to the tuple 'new_nodes'
        new_freq = freqs[0] + freqs[1]
        # sets 'new_freq' to the frequencies of the fisrt 2 nodes added together

        del nodes[0:2]
        # removes the first 2 nodes from 'nodes'
        del freqs[0:2]
        # removes the first 2 frequencies from 'freqs'
        
        for index,item in enumerate(freqs):
            # goes through the list 'freqs' and get the item and index as it does

            if index == 0 and item >= new_freq:
                i = 0
                break
            # if the frequency in 'new_freq' is less then or equal to
            # the index, the variable 'i' is set to 0

            elif freqs[-1] < new_freq:
                i = len(freqs)
                break
            # if the frequency in 'new_freq' is greater than the
            # last item in 'freqs' then 'i' is set to -1 

            elif new_freq <= item:
                i = index
                break
            # if the frequency in 'new_freq' is less than or equal to
            # the item, 'i' is set to the index

        nodes.insert(i, new_node)
        # the node in 'new_node' is inserted into the list 'nodes' at 
        # the index 'i'
        freqs.insert(i, new_freq)
        # the frequency in 'new_freq' is inserted into the list 'freqs'
        # at the index 'i'

    print(f'nodes: {nodes}')
    # the list 'nodes' is printed
    # this is a not very visual representation of the tree, where
    # each item in each tuple is a branch

    encoded_txt = ''
    # creates a string 'encoded_txt' for the encrypted message

    encoded_values = {}
    # creats a dict 'encoded_values' to store the encoded characters

    for char in set(inp):
        encoded_values[char] = "".join(find_nodes(nodes, char))
        # finds the characters paths and adds it to the dict 'encoded_values'

    print(f'encoded values: {encoded_values}')
    # prints out the dict 'encoded values'

    for char in inp:
        encoded_txt += encoded_values[char]
        # adds the encoded characters to the message
    
    print(f'encoded message: {encoded_txt}')
    # pritnts out the encoded message
    
    return [encoded_txt, nodes]
    # 

tree_making()
# runs the function 'encoding'



        
