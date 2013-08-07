#!/usr/bin/env python3

import math
import random


def game():
    j = 1
    sum_one = sum_two = count_one = count_two = 0

    for looper in range(20):
        if sum_one < 20:
            sum_one += math.ceil(int(random.random() * 10) * j)
            count_one += 1
        if sum_two < 20:
            sum_two += math.ceil(int(random.random() * 10) * j)
            count_two += 1
        looper += 1
        if looper > 7:
            looper = 1

    if (count_one < count_two):
        print("P1 wins with Count: ", count_one)
    elif (count_one > count_two):
        print("P2 wins with Count: ", count_two)
    else:
        print("P1 and P2 are drawn ! :P ")

for each in range(20):
    game()
