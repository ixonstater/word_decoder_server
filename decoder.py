from itertools import permutations
import enchant

def vettInDictionary(perms):
    d = enchant.Dict("en_US")
    words = []
    for perm in perms:
        if(d.check(perm)):
            words.append(perm)
    words = list(set(words))
    words.sort(key = len, reverse = True)
    return words

def generatePermutations(letters):
    perms = []
    words = []
    for length in range(6, 2, -1):
        perms += list(permutations(letters, length))
    for perm in perms:
        words.append("".join(perm))
    return words

# def main():
#     print(vettInDictionary(generatePermutations(['n','a','d','l','i','e'])))

# if __name__ == '__main__':
#     main()