# ------- For Loops and Fancy String Manipulation

# ---- Loops over string

def has_vowel(s):
    ''' (str) -> bool
    Return True if and only if s has at least one vowel, not including y.

    >>> has_vowel("Anniversary")
    True
    >>> has_vowel ("xyz")
    False
    '''
    vowel_found = False
    for char in s:
        if char in 'aeiouAEIOU':
            vowel_found = True
    return vowel_found


def collect_vowels(s):
    ''' (str) -> str
    Return the vowels from s.
    Do not treat the letter y as a vowel.
    
    >>> collect_vowels("Happy Anniversary!")
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    '''
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
    return vowels


def count_vowels(s):
    ''' (str) -> int
    Return the number of vowels in s.
    Do not treat the letter y as a vowel.

    >>> count_vowels("Happy Anniversary!")
    5
    >>> count_vowels('xyz')
    0
    '''

    num_vowels = 0

    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels


#---------------- w4 - ex 14
def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that
    appear at leastonce in s2. The characters in the result
    will appear in the same order asthey appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abb', 'ab')
    'abb' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''

    res = ''
    for ch in s1:
        if ch in s2:
            res = res + ch
    
    return res

#---------------- w4 - ex 13
def ex13a(message):
    '''
    >>> ex13a('Happy 29th!')
    Happy 30th!
    '''
    message = 'Happy 29th!'
    new_message = ''

    for char in message:
        if char.isdigit():
            new_message = new_message + str((int(char) + 1) % 10)
        else:
            new_message = new_message + char

    return new_message


def ex13b(message):

    '''
    >>> ex13b('Happy 29th!')
    Happy 3209th!
    '''
    message = 'Happy 29th!'
    new_message = ''

    for char in message:
        if not char.isdigit():
            new_message = new_message + char
        else:
            new_message = new_message + str((int(char) + 1) % 10)

    return new_message


#---------------- w4 - ex 12
def ex12(digits):
    '''
    Print each duplicate digit
    >>> ex12('0123456789')
    00112233445566778899
    '''
    result = ''

    for digit in digits:
        result = result + digit * 2

    return result

#---------------- w4 - ex 11
def ex11(digits):
    '''
    Returns the last digit of the parameter
    >>> ex11('0123456789')
    9
    '''
    result = 0

    for digit in digits:
        result = digit

    return result

#---------------- w4 - ex 10
def ex10(digits):
    '''
    Subtracts each digit from the result
    >>> ex10('0123456789')
    55
    '''
    digits = '0123456789'
    result = 100

    for digit in digits:
        result = result - int(digit)

    return result
