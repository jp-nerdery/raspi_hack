#!/usr/bin/env python
# -*- coding:utf-8 -*-

# require memory_profiler
# pip install memory_profiler
from memory_profiler import profile 

@profile
def test1(index):
    """
    関数の実行速度を計測する
    return: none
    
    Example
    input:[[1,2,2],[1,2,3]]
    return:[[ 0.  1.]
            [ 1.  0.]]   
    """

    a = range(index)

if __name__ == "__main__":
    test1(2**20)