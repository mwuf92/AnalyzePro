# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:52:23 2023

@author: hp
"""

class BasicCal:
    def sum_two_nums(self, num1, num2):
        res = num1 + num2
        print(res)
        return res
    def subtract_two_nums(self, num1, num2):
        res = num1 - num2
        print(res)
        return res
    def multi_two_nums(self, num1, num2):
        res = num1 * num2
        print(res)
        return res
    def divide_two_nums(self, num1, num2):
        if num2 == 0:
            print("wrong input")
        res = num1 / num2
        print(res)
        return res