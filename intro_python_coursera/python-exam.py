# work file for exam course python fundamentals

def larger_of_smallest(L1, L2):
    '''(list of int, list of int) -> int

    Return the larger of the smallest value in L1 and the small    est value inL2.

    Precondition: L1 and L2 are not empty.

    >>> larger_of_smallest([1, 4, 0], [3, 2])
    2
    >>> larger_of_smallest([4], [9, 6, 3])
    4
    '''

   return max(min(L1), min(L2))
   
   
   def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the       letters in prefix.
    '''
    if s1.startswith(prefix) and s2.startswith(prefix):
        return True
    else:
        return False
        
    #return s1.startswith(prefix) and s2.startswith(prefix) 
    
    
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
    
    result = ""
    i = len(s) - 1

    while i >= 0:
        result = result + s[i]
        i = i - 1
    return result


def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for k in d:
        if k in L:
            result.append(k)

    return result


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
        if d[k] in d:
             result = result + 1

    return result


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
            d[c] = 1
        else:
            d[c] = d[c] + 1

    return d
