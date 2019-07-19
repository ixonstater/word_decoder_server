from itertools import permutations
import enchant

def vettInDictionary(perms):
    d = enchant.Dict("en_US")
    words = []
    for perm in perms:
        if(d.check(perm)):
            words.append(perm)
    return list(set(words))

def generatePermutations(letters):
    perms = []
    words = []
    for length in range(6, 2, -1):
        perms += list(permutations(letters, length))
    for perm in perms:
        words.append("".join(perm))
    return words