#!/usr/bin/env python
# -*- coding:utf-8 -*-

# require memory_profiler
# pip install memory_profiler
from memory_profiler import profile 

@profile
def test1(index):
  a = range(index)

if __name__ == "__main__":
  test1(2**20)