def colour_to_fruit(L):
    ''' (dict of (str: str) -> dict of (str:str)
    Invert fruit to colour

    >>> fruit_colour = {
        'banana': 'yellow',
        'cherry': 'red',
        'orange': 'orange',
        'pear': 'green',
        'peach': 'orange',
        'plum': 'purple',
        'pomegranate': 'red',
        'strawberry': 'red'}
    >>> colour_to_fruit(fruit_colour)
        {'yellow': ['banana'],
         'red': ['cherry', 'pomegranate', 'strawberry'],
         'orange': ['orange', 'peach'],
         'green': ['pear'],
         'purple': ['plum']}
    '''
    colour_fruit = {}
    for fruit in L:
        colour = L[fruit]

        # if colour is not already a key in the accumulator,
        # add colour: [fruit] as an entry
        if not (colour in colour_fruit):
            colour_fruit[colour] = [fruit]

        # otherwise, append fruit to the existing list
        else:
            colour_fruit[colour].append(fruit)
    return colour_fruit

#### ------------------------------ WEEK 7 - EX 11

def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of that fruit.

    Try to eat one of each fruit, reduce by 1 all quantities greater than 0
    associated with each fruit in d and return TRUE if and only fruit was eaten.

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:

        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate


#### ------------------------------ WEEK 7 - EX 12

def contains12a(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in d.
    >>> contains12a('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]})
    True
    >>> contains12a('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE
    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True
 
    return found

def contains12b(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in d.
    >>> contains12b('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]})
    True
    >>> contains12b('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE
    for k in d:
        if v in d[k]:
            found = True
 
    return found

#### ------------------------------ WEEK 7 - EX 05
def smaller_of_largest(L1, L2):
    '''(list of int, list of int) -> int

    Return the smaller of the largest value in L1 and the largest value inL2.

    Precondition: L1 and L2 are not empty.

    >>> smaller_of_largest([1, 4, 0], [3, 2])
    3
    >>> smaller_of_largest([4], [9, 6, 3])
    4
    '''

    return min(max(L1),max(L2)) # CODE MISSING HERE

### ------------------------------ WEEK 7 - EX 06
def same_length(L1, L2):
    '''(list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    >>> same_length([1, 4, 0], [3, 2])
    False
    >>> same_length([1, 4, 0], [3, 2, 1])
    True
    '''

    #if len(L1) == len(L2):
    #   return True
    #else:
    #   return False

    return len(L1) == len(L2)

#### ------------------------------ WEEK 7 - EX 08
def reverse(s):
    '''(str) -> str

     Return the reverse of s.

     >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    '''

    result = ''
    i = len(s) - 1
    while i >= 0:
        result = result + s[i]
        i = i - 1# CODE MISSING HERE

    return result

#### ------------------------------ WEEK 7 - EX 09
def get_keys(L, d):

    '''(list, dict) -> list
    Return a new list containing all the items in L that are keys in d.
    >>>get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    >>>get_keys([0, 'a', 'b'], {'b': 3, 'a': 2, 4: 'w'})
    ['a', 'b']
    '''

    result = []
    for k in L:# CODE MISSING HERE
        if k in d:
            result.append(k)
    return result

#### ------------------------------ WEEK 7 - EX 10
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        

        #if d[k] in list(d.keys()): Your answer should only use operator in, variables k and d, and indexing. Do not use parentheses.
        print(k)
        print(d[k])
        print(d)
        if d[k] in d: # CODE MISSING HERE
             result = result + 1

    return result

#### ------------------------------ WEEK 7 - EX 11
def double_last_value(L):
    '''(list of int) -> NoneType

    Double the value at L[-1]. For example, if L[-1] is 3,
    replace it with 6.

    Precondition: len(L) >= 1.
    >>> L1 = [1, 3, 5]
    >>> double_last_value(L1)
    10
    '''
    return (L[-1] * 2)

#### ------------------------------ WEEK 7 - EX 12

def get_diagonal_and_non_diagonal12a(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal12a([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            # CODE MISSING HERE
            if row == col:
                diagonal.append(L[row][col])
            elif row != col:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

def get_diagonal_and_non_diagonal12b(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal12b([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            # CODE MISSING HERE
            if row == col:
                diagonal.append(L[row][col])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

def get_diagonal_and_non_diagonal12c(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal12c([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            # CODE MISSING HERE
            if row == col:
                diagonal.append(L[row][col])
            if row != col:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

def get_diagonal_and_non_diagonal12d(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal12d([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            # CODE MISSING HERE
            if row == col:
                diagonal.append(L[row][row])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

#### ------------------------------ WEEK 7 - EX 13
def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c] = d[c] + 1    # CODE MISSING HERE




#------------------------ w7 - Understand List and Dictionary

def print_list_dict():
    my_list = [1, 2, 'a']
    my_dict = {'b': 3, 'a': 2, 4: 'w'}

    for i in my_list:
        print(i)
        
    print()

    for j in my_dict:
        print(j, my_dict[j])
        
    # Output
    #1
    #2
    #a

    #b 3
    #a 2
    #4 w

#------------------------- 
    
def count_chars(s):

    '''(str) -> dict of {str: int}
    Return a dictionary where the keys are the characters in s and the values

    are how many times those characters appear in s.

    >>> count_chars('abracadabra')

    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}

    '''

    d = {}
    for c in s:
        if not (c in d):
          
            d[c] = 1  # CODE MISSING HERE

        else:
            d[c] = d[c] + 1
 
    return d

#--------------------------------- 
def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths
    of the strings in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    >>> are_lengths_of_strs([4, 0, 2, 5], ['abcd', '', 'ef'])
    False
    >>> are_lengths_of_strs([4, 0, 2, 5], ['abcd', '', 'ef', 'we'])
    False
    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef','we'])
    True
    '''
    
    result = True
    if len(L1) > len(L2):
        return False

    for i in range(len(L1)):
        if L1[i]!=len(L2[i]):
            result = False
            
    return result

#--------------------------------------

def gather_every_nth(L, n):
    '''(list, int) -> list
 
    Return a new list containing every n'th element in L, starting at index 0.
 
    Precondition: n >= 1
 
    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''
 
    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n
 
    return result
 

