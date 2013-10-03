# -*- coding:utf-8 -*-
"""
    CryptArithmetic puzzle.
    Send More Money puzzle

"""

import itertools
import time
import re

# Solve puzzle
#
#       S E N D
#   +   M R O E
#  -------------
#     M O N E Y

# send = s * 1000 + e * 100 + n * 10 + d
# more = m * 1000 + r * 100 + o * 10 + e
# money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
# money = send + more


def Calculate():
    m = 1
    t = 0
    start = time.clock()
    try:
        for s in range(10):
            for e in range(10):
                for n in range(10):
                    for d in range(10):
                        for r in range(10):
                            for o in range(10):
                                for y in range(10):
                                    t += 1
                                    if distinct(s, e, n, d, m, o, r, y):
                                        send = s * 1000 + e * 100 + n * 10 + d
                                        more = m * 1000 + o * 100 + r * 10 + e
                                        money = m * 10000 + o * \
                                            1000 + n * 100 + e * 10 + y
                                        if money == (send + more):
                                            print "Calculate times :%s ; take times: %s ; Answer: " % (t, time.clock()-start)
                                            print " send : %s%s%s%s" % (s, e, n, d)
                                            print " more : %s%s%s%s" % (m, o, r, e)
                                            print "money :%s%s%s%s%s" % (m, o, n, e, y)
                                            raise Exception('Found!')
    except Exception as data:
        pass
        # print "Calculate times :%s Answer: " %t
        # print " send : %s%s%s%s" %(s,e,n,d)
        # print " more : %s%s%s%s" %(m,o,r,e)
        # print "money :%s%s%s%s%s" %(m,o,n,e,y)


def solve2():
    start = time.clock()
    letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        send = 1000 * sol['s'] + 100 * sol['e'] + 10 * sol['n'] + sol['d']
        more = 1000 * sol['m'] + 100 * sol['o'] + 10 * sol['r'] + sol['e']
        money = 10000 * sol['m'] + 1000 * sol[
            'o'] + 100 * sol['n'] + 10 * sol['e'] + sol['y']
        if send + more == money:
            print "take times : %s" % (time.clock() - start)
            return send, more, money


def distinct(*args):
    return len(set(args)) == len(args)


def solve3(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    print 'first_letters %s' % first_letters
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    print sorted_characters
    characters = tuple(ord(c) for c in sorted_characters)
    print characters
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation


# print solve2()
# Calculate()
print solve3("I + LOVE + YOU == DORA")
