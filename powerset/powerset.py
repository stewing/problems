#!/usr/local/bin/python3.6

from pprint import pprint, pformat

# The power set of a set is the set of all its subsets. Write a function that,
# given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3},
# {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

def powerset(inpset, sets=None, idx=0):
    if sets is None:
        sets = [set()]
        sets.append(set(inpset))

    if idx == len(inpset):
        return sets

    for ix in range(idx, len(inpset)):
        nset = set([inpset[idx], inpset[ix]])
        if nset not in sets:
            sets.append(nset)

    idx = idx + 1
    powerset(inpset, sets, idx)

    return sets
        
set1 = [1, 2, 3]
print("input: {}\n  output: {}".format(pformat(set1), pformat(powerset(set1))))

set2 = [1, 2, 3, 4]
print("input: {}\n  output: {}".format(pformat(set2), pformat(powerset(set2))))
