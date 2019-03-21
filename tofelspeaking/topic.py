# -*- coding: utf-8 -*-
# @Author: orres
# @Email:  jasonjin22@gmail.com
# @Date:   2019-03-21 10:29:19
# @Last Modified by:   orres
# @Last Modified time: 2019-03-21 10:48:35
# This is a simulating program of TOFEL speaking section(especially for part one and two)
# The topics in the "tofel speaking 80.txt" is collected from the internet

import random
import time
import os

file = open("../docs/tofel speaking 80.txt").read()
array = file.split('\n')

def timeCount(duration):
    lineLength = duration
    delaySeconds = 1
    frontSymbol = '='
    frontSymbol2 = ['—', '\\', '|', '/']
    backSymbol  = ' '
    lineTmpla = "{:%s<%s} {} {:<2}"%(backSymbol, lineLength)
    for j in range(lineLength):
        tmpSymbol = frontSymbol2[j%(len(frontSymbol2))]
        print("\r" + lineTmpla.format(frontSymbol * j, tmpSymbol, j), end='')
        time.sleep(delaySeconds)

def assignTopic():
    index = random.randint(0, 79)
    print(50*"#")
    print(array[index])
    print(50*"#")
    time.sleep(7)
    os.system('say "you have fifteen seconds to prepare and forty-five seconds to speak"')
    timeCount(15)
    print("\n")
    os.system('say "now speak"')