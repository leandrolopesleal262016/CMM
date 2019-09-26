##!/usr/bin/env python3
# coding=UTF-8

import os
import time

os.system("sudo supervisorctl stop cmm")
time.sleep(2)
os.system("sudo supervisorctl start cmm")
