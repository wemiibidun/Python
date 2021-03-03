def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    x = len(dna)
    return x


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if dna1 > dna2:
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    y = dna.count(nucleotide)
    return y


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False
        
def is_valid_sequence(dna):
    
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid

    >>> is_valid_sequence('ATGPcGBa')
    false
    >>> is_valid_sequence('u')
    False

    """
    valid_status = True
    
    for x in dna:
        if x not in ['A','T','C','G']:
            valid_status = False
##            print(x, "is not a valid nucleotide!")
##        else:
##            print(x, "is a valid nucleotide!")
            
    return valid_status

def insert_sequence(dna1,dna2,int):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index. 

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 3)
    CCGATG
    >>> insert_sequence('CCGG', 'AT', 4)
    CCGGAT
    >>> insert_sequence('CCGG', 'AT', 0)
    ATCCGG
    >>> insert_sequence('CCGGAATTGG', 'AT', 6)
    CCGGAAATTTGG
    
    """
    x = dna1[:int]
    y = dna1[int:]
    insert_sequence = x + dna2 + y
    return insert_sequence



def get_complement(dna):
    
    """ (str) -> str

    Return the nucleotide's complement.  

    >>> get_complement('ACGTACG')
    'TGCATGC'
    
    """
    
    comp = []
    for i in dna:
        if i == "T":
            comp.append("A")
        if i == "A":
            comp.append("T")
        if i == "G":
            comp.append("C")
        if i == "C":
            comp.append("G")

    return ''.join(comp)


def get_complementary_sequence(dna):
    
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence  

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('WI')
    'WI'
    
    """
    return dna[::-1]
