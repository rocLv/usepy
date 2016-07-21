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


def solve():
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


def distinct(*args):
    return len(set(args)) == len(args)


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


def solveAll(puzzle):
    print '> Be patient for a while ...'
    puzzle = puzzle.split(' ')
    puzzle = ''.join(puzzle).upper()
    # Find all the words in the expression, but keep the sequence.
    words = re.findall('[A-Z]+', puzzle)
    # Find all the sign in the expression, also keep the sequence.
    sign = re.findall('\W', puzzle)
    unique_char = set(''.join(words))
    assert len(unique_char) <= 10, 'Too many letters'
    # first letter of words
    first_letters = {w[0] for w in words}
    found_solution = False
    for per in itertools.permutations(tuple(range(0, 10)), len(unique_char)):
        dic_letter_value = dict(zip(unique_char, per))
        # First letter of word can NOT be zero, filter them.
        zero = False
        for (k, v) in dic_letter_value.items():
            if v == 0 and k in first_letters:
                zero = True
                break
        if zero:
            continue

        # print 'trying ',dic_letter_value
        # test for send+more=money
        # dic_letter_value={'S':9,'E':5,'N':6,'D':7,'M':1,'O':0,'R':8,'E':5,'Y':2}   # test for send+more+money
        # dic_letter_value={'I':1,'L':5,'O':8,'V':4,'E':2,'Y':9,'U':7,'D':6,'R':3,'A':0}  # test for i+love+you=dora
        # Calculate every possible
        dic_words_value = dict()
        for w in words:
            dic_words_value[w] = calculateSingleWordValue(w, dic_letter_value)
        # Calculate value of two part of '='
        left_exp, left_value = calculateExpressionValue(
            words[0:-1], sign[0:-1], dic_words_value)
        right_exp, right_value = calculateExpressionValue(
            [words[-1]], [], dic_words_value)
        # print left_exp,left_value
        # print right_exp,right_value
        # print dic_words_value
        # assert left_value != right_value,'Got it ! %s %s' %
        # (puzzle,dic_words_value)
        if left_value == right_value:
            found_solution = True
            print "> Got one: %s %s" % (puzzle, dic_words_value)
            continue
    if not found_solution:
        print '> NO FOUND! Bad luck! -_-|||'
    else:
        print '> Task complete !'


def calculateExpressionValue(sortedWords, sortedSign, dic_words_value):
    expression = ''
    for i, w in enumerate(sortedWords):
        expression += str(dic_words_value[w])
        if i < len(sortedSign):
            expression += sortedSign[i]
    return expression, eval(expression)


def calculateSingleWordValue(word, dic):
    value = ''
    for w in word:
        value += str(dic[w])
    return value

#print solve2()
#solve()
#solveAll('aa+b=bb')
#solveAll("I + love + YOU = dora")    #1+5842+987=6830
solveAll('eat + that = apple')   # 819+9219=10038
#solveAll('take + a + cake = kate')    #3961+9+2961=6931
#solveAll("send +more= money")    #9567+1085=10652
#solveAll('no + gun + no = hunt')  #87+908+87=1082
#solveAll('base+ball=games')   #7843+7455=14938
#solveAll('cross + roads = danger')    #96233+62513=158746
#solveAll('k * aka = dyna')    # 7*575=4025  6*262=1572
#solveAll('count - coin = snub')   #10652-1085=9567
#solveAll('one + two + five = eight')  #621+846+9071=10538
#solveall('woods + woods + woods = forest')   #71156+71156+71156 = 213468
