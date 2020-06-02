# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:46:52 2020

@author: Home
"""


import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/Home/Desktop/documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)