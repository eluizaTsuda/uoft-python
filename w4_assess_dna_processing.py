def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    result = False
    
    if len(dna1) > len(dna2):
        result = True

    return result

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    if nucleotide != "":
        count = dna.count(nucleotide)

    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence (dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is,
    it contains no characters other than ’A’, ’T’, ’C’ and ’G’).

    >>>is_valid_sequence ('ACTG')
    True
    >>>is_valid_sequence ('XACTG')
    False
    >>>is_valid_sequence ('AcTG')
    False
    >>>is_valid_sequence ('ACCTGGAT')
    True
    """
    result = True

    for char in dna:
        if not char in 'ATCG':
            result = False
            
    return result



def insert_sequence (dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>>insert_sequence ("CCGG", 'AT', 2)
    'CCATGG'
    >>>insert_sequence ("CCGG", 'AT', 0)
    'ATCCGG'
    >>>insert_sequence ("CCGG", 'AT', 4)
    'CCGGAT'
    >>>insert_sequence ("CCGG", 'AT', -3)
    'CATCGG'

    """
    return dna1[:index] + dna2 + dna1[index:]
    

    
def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.
    A and T can be bonded together, and thus complement each other;
    similarly, C and G are complements of each other.

    >>>get_complement('A')
    T
    >>>get_complement('T')
    A
    >>>get_complement('C')
    G
    >>>get_complement('G')
    C
    >>>get_complement('')
    >>>get_complement('x')
    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def get_complementary_sequence(dna):
    """(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('ACTG')
    'TGAC'
    >>>get_complementary_sequence('')
    ''
    >>>get_complementary_sequence('PACT')
    'TGA'

    """
    result = ''
 
    for char in dna:
        if char == 'A':
            result = result + 'T'
        elif char == 'T':
            result = result + 'A'
        elif char == 'C':
            result = result + 'G'
        elif char == 'G':
            result = result + 'C'
            
    return result
 
