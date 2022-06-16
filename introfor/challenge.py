#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""

import yaml
import crayons

with open('farms.yaml', 'r') as farmfile
    farms = yaml.safe_load(farmfile)


