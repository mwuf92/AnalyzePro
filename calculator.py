# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:31:19 2023

@author: hp
"""
import matplotlib.pyplot as plt
import numpy as np

from basicCal import BasicCal
from scientificCal import ScientificCal
from advancedCal import AdvancedCal

while True:
    cal_type = input("Which calculator: \n b for basics\n a for advanced\n s for scientific\n q for quite\n")
    if cal_type == "s":
        print(cal_type)
    elif cal_type == "b":
        print(cal_type)
    elif cal_type == "a":
        print(cal_type)
    elif cal_type == "q":
        break
    else:
        print("Wrong")


     
'''basic_cal_obj = BasicCal()

result = basic_cal_obj.sum_two_nums(9, 10)

print("My reesult is: ", result)

result2 = basic_cal_obj.divide_two_nums(8, 2)

print("My reesult is: ", result2)


scientific_cal_obj = ScientificCal()
scientific_cal_obj.test_print()

advanced_cal_obj = AdvancedCal()
advanced_cal_obj.test_print()'''