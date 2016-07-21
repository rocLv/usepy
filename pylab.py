# -*- coding:utf-8 -*-
#
# Copyright [2013] scymen@gmail.com
#

""" Using pylab (matplotlib) for graphics
    Hailstone sequence by Collatz
"""

import sys
import math
#sys.path.append("C:/Python27/Lib/site-packages")
import matplotlib.pyplot as plt

def Hailstone(positive):
    """ Generate a Hailstone sequence """
    list = []
    #stop when sequence reaches 1
    while positive > 1:
        if positive % 2:        # positive is odd
            positive = positive *3 +1
        else:                   #positive is even
            positive = positive /2
        list.append(positive)
    return list


def DrawSineWave():
    """ plot a sine wave from 0 to 4pi
    Args of plot(xvalue,yvalue,colorSign):
        color: r = red, b = blue, g = green, k = black
        sign:   o=circle  .=dot x=x +=plus
    e.g. colorSign='ro' means that draw a red circle.

    """
    xValue = []
    yValue = []
    num = 0.0
    while num < math.pi *4:
        yValue.append(math.sin(num))
        xValue.append(num)
        num += 0.1
    plt.plot(xValue,yValue,'ro')
    plt.show()


num = raw_input("Enter a positive integer:")
num = int(num)
list = Hailstone(num)
plt.plot(list)
plt.show()

DrawSineWave()
