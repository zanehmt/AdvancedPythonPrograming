#Write a function called find_dups that takes a list of integers as its input
#argument and returns a set of those integers occurring two or more times in
#the list
def find_dups(L):

    elem_set = set()
    dups_set = set()
    for entry in L:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return(dups_set)

print(find_dups(([1, 1, 2, 3, 4, 2])))