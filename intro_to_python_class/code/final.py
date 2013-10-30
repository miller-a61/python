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
            d[c]=1 # CODE MISSING HERE
        else:
            d[c] = d[c] + 1

    return d


def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            '''if L[row][col] < 0:
                neg.append(L[row][col])
            elif L[row][col] >= 0:
                nonneg.append(L[row][col])
            '''
            '''if L[row][col] > 0:
                nonneg.append(L[row][col])
            elif L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])'''
            '''if L[row][col] < 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])'''
            '''if L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])'''
            if L[row][col] < 0:
                neg.append(L[row][col])

            nonneg.append(L[row][col])
                
    return (neg, nonneg)

def double_last_value(L):
    '''(list of int) -> NoneType

    Double the value at L[-1].  For example, if L[-1] is 3,
    replace it with 6.

    Precondition: len(L) >= 1.
    '''

    L[-1] = L[-1]*2


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
        if d[k] in d:  # CODE MISSING HERE
            result = result + 1

    return result


def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for k in d: # CODE MISSING HERE
        if k in L:
            result.append(k)

    return result


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
        i = i-1 # CODE MISSING HERE

    return result



def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    '''

    '''if s1.startswith(prefix) and s2.startswith(prefix):
        return True
    else:
        return False
    '''

    return s1.startswith(prefix) and s2.startswith(prefix)
    


def smaller_of_largest(L1, L2):
    '''(list of int, list of int) -> int

    Return the smaller of the largest value in L1 and the largest value in
    L2.

    Precondition: L1 and L2 are not empty.

    >>> smaller_of_largest([1, 4, 0], [3, 2])
    3
    >>> smaller_of_largest([4], [9, 6, 3])
    4
    '''

    return min(max(L1),max(L2))

    # CODE MISSING HERE


'''The expression for the return statement is missing.
Write it below. Use only the parameters, one call on function min,
and two calls on function max.

Do not use unnecessary parentheses: you need them for the function calls,
but nothing else. Do not include the word return; just write the expression.
'''
