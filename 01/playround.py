#!/usr/bin/python
# coding=utf-8
# input
import random

stages = 410
chance = 8
stage_range = range(1, stages + 1)
print(random.choice(stage_range))
# output
result = [random.choice(stage_range) for x in range(0, 8)]
print(result)
