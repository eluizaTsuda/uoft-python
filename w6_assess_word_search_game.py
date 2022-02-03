"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""
#================

def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>>is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TOO')
    False
    >>>is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'BOX')
    True
    """

    for i in range(0,len(wordlist)):
        if word == wordlist[i]:
            return True
    return False

#================
    
def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>>make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], -1)
    'XSOB'
    make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], -2)
    'ANTT'
    make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], -3)
    ''
    make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2)
    ''
    """

    single_string = ""

    if row_index > len(board)-1 or row_index < len(board) * (-1):
        return single_string
           
    for i in range(0,len(board[row_index])):
        single_string = single_string + board[row_index][i]

    return single_string

#================

def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['L', 'I', 'Z']], 1)
    'NSI'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['L', 'I', 'Z']], 3)
    'TB'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 4)
    ''
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], -4)
    'AX'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], -5)
    ''
    """

    single_string = ""
    
    for i in range(0, len(board)):
        
        if column_index <= len(board[i])-1 and column_index >= len(board[i]) * (-1):
            single_string = single_string + board[i][column_index]
    return single_string

#================

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False

#================
def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>>board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NS')
    True
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO')
    True
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TB')                          
    True
    >>>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'AS')
    False
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SA')
    False
    """
    
    for col_index in range(0, len(board[0])):
        if word in make_str_from_column(board, col_index):
            return True    
    return False
    
#================

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ATT')
    False
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TB')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TX')
    False
    """

    # check - row
    result_row = board_contains_word_in_row(board, word.upper())

    # check - column
    if result_row == True:
        return True
    else:
        return (board_contains_word_in_column(board, word.upper()))

#================

def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('DR')
    0
    >>> word_score('DRU')
    3
    >>> word_score('DRUDGE')
    6
    >>> word_score('DRUDGER')
    14
    >>> word_score('DRUDGERYP')
    18
    >>> word_score('DRUDGERYPQ')
    30
    >>> word_score('DRUDGERYPQA')
    33
    """

    len_word = len(word)

    if len_word < 3:
        return 0
    elif 3 <= len_word <= 6:
        return len_word
    elif 7 <= len_word <= 9:
        return (len_word * 2)
    else:
        return (len_word * 3)
    
#================ update_score(player_info, word)
    
def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """

    player_info[1] = player_info[1] + word_score(word)

#================

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['BOX', 'BT'])
    0
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['BOX', 'TB'])
    1
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO', 'NTT', 'OB', 'TB', 'BT'])
    6
    """

    count_words = 0

    for i in range(0, len(words)):
        result = board_contains_word(board, words[i])
        if result == True:
            count_words = count_words + 1
            
    return count_words

#-----------------------------

def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    words_list = []

    line = words_file.readline()

    while line != '':
        words_list.append(line.strip())
        line = words_file.readline()

    return words_list

#-----------------------------

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """

    board_list = []
    lst_of_lst = []
    line = board_file.readline()

    while line != '':
        board_list.append(line.strip())
        line = board_file.readline()

    # ------ FROM  lst of str TO lst of lst of str
    # ------ return ([list(i) for i in board_list])

    for word in board_list:
        lst_of_lst.append([n for n in word])

    return lst_of_lst

#-----------------------------
