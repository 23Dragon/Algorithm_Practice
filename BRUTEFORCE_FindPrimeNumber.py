import math
from itertools import permutations

def solution(numbers):
    answer = 0
    
    # prime number check function
    def is_prime(number):
        if number == 0 or number == 1:
            return False

        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                return False
        return True
    
    # do permutations        
    ls = set()
    for i in range(1, len(numbers)+1):
        ls |= set(map(int, map(''.join, permutations(numbers, i))))

    # check prime numbers
    prime_numbers = [int(x) for x in ls if is_prime(int(x)) is True]

    answer = len(prime_numbers)
    return answer

solution("011")
