# week 6 For Loops Over indices, Parallel and Nested Lists and Strings, and Files
#

# For Loops Over Indices

def count_matches(s1, s2):
    ''' (str, str) -> int
    
    Return the number of positions in s1 that contain the
    same character at the corresponding position of s2.
    
    Precondition: len(s1) == len(s2)
    
    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    '''

    num_matches = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches
    

def sum_items(list1, list2):
    ''' (list of number, list of number) -> list of number
    
    Return a new list in which each item is the sum of the items at the
    corresponding position of list1 and list2.
    
    Precondition: len(list1) == len(list2)
    
    >> sum_items([1, 2, 3], [2, 4, 2])
    [3, 6, 5]
    '''

    sum_list = []

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list

        
    

def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    >>>shift_left([3, 6, 5])
    [6, 5, 3]
    '''
    
    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item

    return L
    

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats

#=======================================================

# NESTED LISTS AND STRING

def averages(grades):
    '''
    (list of list of number) -> list of float

    Return a new list in which each item is the average of the
    grades in the inner list at the corresponding position of
    grades.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []

    for grades_list in grades:
        # Calculate the average of grades_list and append it
        # to averages.

        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages


def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float

    Return the average of the grades in asn_grades
    >>> calculate_average([['A1', 80],['A2', 90]])
    85.0
    '''

    total = 0
    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)


#========================================================

#13 1 ok

def write_to_file131(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.

    >>>import tkinter.filedialog
    >>>a1_quiz13 = tkinter.filedialog.asksaveasfilename()
    >>>a1_histfile = open(a1_quiz13, 'w')
    >>>write_to_file131(a1_histfile, ['Eu', ' vou', ' acertar', ' tudo'])
    >>>a1_histfile.close()
    Eu
     vou
     acertar
     tudo
    """

    # CODE MISSING HERE
    for s in sentences:
        file.write(s + '\n')

#========================================================
#13 2
def write_to_file132(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    >>>import tkinter.filedialog
    >>>a1_quiz13 = tkinter.filedialog.asksaveasfilename()
    >>>a1_histfile = open(a1_quiz13, 'w')
    >>>write_to_file132(a1_histfile, ['Eu', ' vou', ' acertar', ' tudo'])
    >>>a1_histfile.close()
    Eu
     vou
     acertar
     tudo
    """

    # CODE MISSING HERE
    for s in sentences:
        file.write(s)
        file.write('\n')

#========================================================
#12 1

def lines_startswith121(file, letter):
    """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

    Precondition: len(letter) == 1

    
    >>>import tkinter.filedialog
    >>>a1_quiz12 = tkinter.filedialog.askopenfilename()
        Open file w6_txt_lines_startswith_ex12.txt
            Aparecida
            EsperAnca
            Cida
            Anjo da Guarda
            aClementina
            Cidalia
            Cinefala
            Denislandia
            Euricledes
            aqueceliA
            
    >>>a1_file = open(a1_quiz12, 'r')
    >>>lines_startswith121(a1_file, 'A')
    ['Aparecida', 'Anjo da Guarda']
    """

    matches = []

    # CODE MISSING HERE
    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))

    return matches
#========================================================
#12 2
def lines_startswith122(file, letter):
    """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.
     The lines should have the newline removed.

    Precondition: len(letter) == 1

    >>>import tkinter.filedialog
    >>>a1_quiz12 = tkinter.filedialog.askopenfilename()
        Open file w6_txt_lines_startswith_ex12.txt
            Aparecida
            EsperAnca
            Cida
            Anjo da Guarda
            aClementina
            Cidalia
            Cinefala
            Denislandia
            Euricledes
            aqueceliA
            
    >>>a1_file = open(a1_quiz12, 'r')
    >>>lines_startswith122(a1_file, 'A')
    ['Aparecida', 'Anjo da Guarda']
    """

    matches = []

    # CODE MISSING HERE
    for line in file:
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))

    return matches

#========================================================
#9 1
def contains91(value, lst):
   """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested
   lists in lst.

   >>> contains91('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],[80, 100]])
   True
   """

   found = False  # We have not yet found value in the list.

   # CODE MISSING HERE
   for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
   
   return found
#========================================================
#9 2
def contains92(value, lst):
   """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested
   lists in lst.

   >>> contains92('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],[80, 100]])
   True
   """

   found = False  # We have not yet found value in the list.

   # CODE MISSING HERE
   for sublist in lst:
        if value in sublist:
            found = True
   
   return found

#========================================================
#5 1


def make_pairs51(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs51(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    # CODE MISSING HERE
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])

    return pairs
#========================================================
#5 2
def make_pairs52(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs52(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    # CODE MISSING HERE
    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)

    return pairs
#========================================================

#4 1

def shift_right1(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the
    last item to the first position.

    Precondition: len(L) >= 1

    >>>shift_right1(["a", "b", "c", "d"])
    ['d', 'a', 'b', 'c']
    
    >>>L=[1,3,5,7,9,11]
    >>>shift_right1(L)
    [11, 1, 3, 5, 7, 9
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE
    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item

    return L

#========================================================

#3
def mystery3(s):
    """ (str) -> bool
    Return TRUE if and only if 's' is equal to the reverse o 'S'

    >>>mystery3('cici')
    False
    >>>mystery3('ciic')
    True
    >>>mystery3('loveevol')
    True
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)
#========================================================

#2
def mystery(s):
    """ (str) -> bool
    """
    matches = 0  
    print("here 1 ")
    for i in range(len(s) // 2):
        print(range(len(s) // 2))
        print("s[i] = " + s[i])
        print(s[len(s) - 1 - i])
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is this line reached?
                                      # Answer 2 times
            matches = matches + 1

            print("matches = " + matches)

    return matches == (len(s) // 2)

#========================================================

#1
def merge(L):
    '''
    Returns the sum of every three numbers
    >>>print(merge([1,2,3,4,5,6,7,8,9]))
    [6, 15, 24]
    '''
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged
