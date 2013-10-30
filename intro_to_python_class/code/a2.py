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

    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nuc = 0

    for char in dna:
        if char == nucleotide:
            num_nuc = num_nuc + 1

    return num_nuc
    

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


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ACTG')
    True
    >>> is_valid_sequence('AcTG')
    False
    >>> is_valid_sequence('A1TG')
    False
    '''

    valid_seq = True

    for char in dna:
        if char not in 'ATCG':
            valid_seq = False

    return valid_seq

def insert_sequence(dna1, dna2, insert_pos):
    ''' (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.
    (You can assume that the index is valid.)

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence('CCGG','AT',4)
    'CCGGAT'
    >>> insert_sequence('CCGG','AT',0)
    'ATCCGG'
    '''

    return dna1[:insert_pos] + dna2 + dna1[insert_pos:]
    
def get_complement(dna):
    '''(str) -> str

    Return the complementary nucleotide for the nucleotied passed.
    Assume only characters passed are 'C', 'G', 'T', and 'A'.

    >>> get_complement('C')
    'G'
    >>> get_complement('A')
    'T'
    '''

    if dna == 'C':
        return 'G'
    elif dna == 'G':
        return 'C'
    elif dna == 'A':
        return 'T'
    else:
        return 'A'


def get_complementary_sequence(dna):
    '''(str) -> str

    Return the complementary DNA sequence for the sequence passed.
    Assume only characters passed are 'C', 'G', 'T', and 'A'.

    >>> get_complementary_sequence('CGTA')
    'GCAT'
    >>> get_complementary_sequence('AATTAA')
    'TTAATT'
    '''

    comp_seq = ''

    for char in dna:
        if char == 'C':
            comp_seq = comp_seq + 'G'
        elif char == 'G':
            comp_seq = comp_seq + 'C'
        elif char == 'T':
            comp_seq = comp_seq + 'A'
        else:
            comp_seq = comp_seq + 'T'

    return comp_seq
