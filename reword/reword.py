#!/usr/local/bin/python3.6

from pprint import pprint, pformat
from heapq import heappush, heappop, heapify

class chr_cnt():
    def __init__(self, char, cnt):
        self.char = char
        self.cnt = cnt

    def __lt__(self, rhs):
        return self.cnt < rhs.cnt

def reword(inp):
    chrs = {}
    for ch in inp:
        if ch not in chrs:
            chrs[ch] = 1
        else:
            chrs[ch] = chrs[ch] + 1
    
    chq = []
    for xc in chrs:
        chq.append(chr_cnt(xc, chrs[xc] * -1))

    heapify(chq)

    lastch = None
    outstr = ''

    while True:

        if len(chq) == 0:
            break

        mch = heappop(chq)

        if (mch.char == lastch):
            if len(chq) == 0:
                break
            mch2 = heappop(chq)
            heappush(chq, mch)
            mch = mch2
        
        if mch is None:
            break

        outstr = outstr + mch.char
        mch.cnt = mch.cnt + 1
        lastch = mch.char 
        if mch.cnt < 0:
            heappush(chq, mch)
    return outstr

mystr = 'abcab'
print("input: {} output: {}".format(mystr, reword(mystr)))

mystr = 'abbabababccabadabbcab'
print("input: {} output: {}".format(mystr, reword(mystr)))

mystr = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print("input: {} output: {}".format(mystr, reword(mystr)))

mystr = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print("input: {} output: {}".format(mystr, reword(mystr)))

mystr = 'aaabbc'
print("input: {} output: {}".format(mystr, reword(mystr)))

mystr = 'aacccccccccccccccccaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbcccccccccccccccccbbbbbbbb'
print("input: {} output: {}".format(mystr, reword(mystr)))
