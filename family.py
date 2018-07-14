"""
    The family of a number N is defined as the set of numbers
    obtainable by rearranging the digits of N. So the family
    of 255 is 255, 525, 552. Write a function which, given a number
    N, will return the highest member of N's family
"""
def solution(N):
    # convert number to list of digits
    nList = list(str(N))

    # sort list in descending order
    nList.sort(reverse = True)

    # join strings
    largest = ''.join(nList)
    
    return int(largest)
