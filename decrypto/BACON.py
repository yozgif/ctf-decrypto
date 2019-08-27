import re

alpha = 'abcdefghijklmnopqrstuvwxyz'

dic = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab",
            "aabba", "aabbb", "abaaa", "abaab", "ababa", "ababb", "abbaa",
            "abbab", "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb",
            "babaa", "babab", "babba", "babbb", "bbaaa", "bbaab"]

def en(s):
    return ''.join([dic[alpha.index(x)] for x in s if x in alpha])

def de(s):
    e = re.findall("[ab]{5}", s)
    return ''.join([alpha[dic.index(x)] for x in e])