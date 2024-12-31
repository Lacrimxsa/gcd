class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pass


def gcd(a: int, b: int) -> int:
    ''' This is the Euclides's Algorithm:
        The GCD between a and b is the greatest number that divides both without leaving residue.

        Euclides's algorithm it's based on the following observation:
        if b = 0, then GCB(a, b) = a'''
    while b:
        a, b = b, a % b
    return a

def tryModulo(a: int) -> int:
    for i in range(a * 2):
        try:
            print(f" {a} % {i} is: {str(a % i)}")
        except:
            print(f"Error: i is {i}")
    return a

''' For every a % b where b > a, a % b = a '''

x = map(tryModulo, (5,6,7))
''' This doesn't work because map doesn't execute the function immediately, it returns an iterator.
    You need to consume this iterator (using list, for, etc.) for the functions to be executed. '''
x = list(map(tryModulo, (5,6,7)))


'''Map functions work well with lambda functions. Because they are anonymous.
    In this case, we could have tried rewriting the modulo function in a lambda'''





def gcd_(a, b):

    while b:
        a, b = b, a % b

    return a


gcd_(5,10)