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


        
basic_cal_obj = BasicCal()
basic_cal_obj.test_print()

scientific_cal_obj = ScientificCal()
scientific_cal_obj.test_print()

advanced_cal_obj = AdvancedCal()
advanced_cal_obj.test_print()