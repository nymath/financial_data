#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    os.system(f'git add .')
    os.system(f"git commit -m \"update files, {current_time}\"")
    os.system('git push -u origin main')
    print('Success')
except:
    print("ERROR")
