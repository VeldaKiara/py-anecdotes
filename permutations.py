from itertools import permutations
def sync_permutation(str):
    perm_list = permutations(str)
    for perm in list(perm_list):
        print(''.join(perm))
str = input("Enter your string: ")
sync_permutation(str)