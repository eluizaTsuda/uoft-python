# WEEK 5 - While Loops, Lists, and Mutability

# -------------------------
def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s) - 1
    while i >= 0:
         if s[i] in 'aeiouAEIOU':
             return s[i]
         i = i - 1
    return None

# -------------------------

def get_answer(prompt):
    """ (str) -> str

    Use prompt to ask the user for a "yes"or "no"
    answer and continue asking until the user
    gives a valid response. Reurn the answer.
    
    """
    answer = input(prompt)
    
    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer

# -------------------------

def up_to_vowel(s):
    """ (str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    """
    # Before_vowel contains all the characters found in s[0:i]
    # s[0:7] 0123456 | Zymurgy
    # s[0:6] 012345 | Zymurg
    # s[0:5] 01234 | Zymur
    # s[0:4] 0123 | Zymu
    # s[0:3] 012 | Zym
    # s[0:2] 01 | Zy
    # s[0:1] 0 | Z
    # s[0:0] ''
    
    before_vowel = ''
    i = 0

    # Accumulate the non-vowel at the beginning of the string.
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1
    return before_vowel

# -------------------------

def double_even_indices(lst):
    """ (list of int) -> NoneType

    Double every other int in lst, starting at index 0.

    >>>list1 = [11,12,13,14,15,16,17]
    >>>print(list1)
    [11, 12, 13, 14, 15, 16, 17]
    >>>double_even_indices(list1)
    >>>print(list1)
    [22, 12, 26, 14, 30, 16, 34]
    """

    i = 0
    while i < len(lst):
        lst[i] = lst[i] * 2
        i = i + 2

# ---------------------------------------

def double_first_element(lst):
    """
    """
    if len(lst) > 0:
        lst[0] = lst[0] * 2
        
# ---------------------------------------

def interrupted(s):
    """
    """
    s[-1] = "-"
    
# ---------------------------------------

def print_every_third_char(s):
    """
    >>>print_every_third_char('abcABCabcABC')
    a
    A
    a
    A
    """
    for i in range(0, len(s), 3):
        print(s[i])
        print(s[i:i + 1])
# ---------------------------------------
# ex 02
def secret(s):
    '''
    Returns numbers until it finds a letter
    >>>secret('abc123')
    ''
    >>>secret('123abc')
    '123'
    >>>secret('123')
    Error
    '''
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1
   
    return result
# ---------------------------------------
# ex 03

def example(L):
    """ (list) -> list
    Return a list containing every third item from L starting at index 0.
    >>>example([70, 75, 80])
    [70]
    >>>example([70, 80, 90, 100])
    [70, 100]
    >>>example([70, 80, 90, 100, 110, 120, 130])
    [70, 100, 130]
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result
# ---------------------------------------
# ex 04
def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements       from Lconcatenated together, starting with indices 0 and 1,    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE
                
        i = i + 2

    return compressed_list



# ---------------------------------------
# ex 05
def sum_odd_numbers(nfrom, nto):
    """
    Sum of the odd numbers from  x through y, inclusive.

    >>>sum_odd_numbers(1523, 10503)
    27004383
    >>>sum_odd_numbers(23, 51)
    555
    >>>sum_odd_numbers(2, 10)
    24
    """

    count_odd = 0 
    if (nfrom % 2) == 0:
        nfrom = nfrom + 1

    for i in range(nfrom, nto+1, 2):
        count_odd = count_odd + i

    return count_odd
# -- 

def sum_even_numbers(nfrom, nto):
    """
    Sum of the even numbers from  x through y, inclusive.

    >>>sum_even_numbers(524, 10508)
    27541388
    >>>sum_even_numbers(1, 11)
    30
    """

    count_even = 0
    if (nfrom % 2) != 0:
        nfrom = nfrom + 1
        
    for i in range(nfrom, nto+1, 2):
        count_even = count_even + i

    return count_even
# ---------------------------------------
# ex 06 
def while_version(L):
    """ (list of number) -> number
    The while loop stops as soon as an even number is found,
    and the sum of all the previous numbers is returned.
    
    >>>lista = [11,1,3,5,6,4,2,1,0]
    >>>while_version(lista)
    20
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
         i = i + 1

    return total

def for_version(L):
    """ (list of number) -> number
    The for loop stops as soon as an even number is found,
    and the sum of all the previous numbers is returned.
    
    >>>lista = [11,1,3,5,6,4,2,1,0]
    >>>for_version(lista)
    20
    """
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

#-----------------------------------
# ex 09
def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    
    >>> playlist = ['Lola', 'Venus', 'Lola', 'Lola','Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    >>> cap_song_repetition(playlist, 'Lola')
    >>>playlist
    ['Venus', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']

    '''

    #while playlist.count(song) > 3:
    #    playlist.pop(playlist.index(song))

    # or

    while playlist.count(song) > 3:
        playlist.remove(song)

#-----------------------------
# ex 12
def increment_items(L, increment):
    '''
    Add increment to each list value
    >>> values = [1,2,3]
    >>> increment_items(values, 2)
    [3, 4, 5]
    '''
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

    return values
