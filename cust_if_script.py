#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'According to the Saffir-Simpson Hurricane Winds Scale, '

# wind speed in a float() to accept decimals as numbers
wind = float(input("What is the wind speed in km/h? "))

# Category of Hurricane
if ((wind >= 119) and ( wind <= 153)):
    message = message + 'this is a category 1 hurricane'
elif ((wind >= 154) and (wind <= 177)):
    message = message + 'this is a category 2 hurricane'
elif ((wind >= 178) and (wind <= 208)):
    message = message + 'this is a category 3 hurricane (major)'
elif ((wind >= 209) and (wind <= 251)):
    message = message + 'this is a category 4 hurricane (major)'
elif wind >= 252:
    message = message + 'this is a category 5 hurricane (major)'
else:
    message = message + 'this is not a hurricane'
print(message)

