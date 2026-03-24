import sys
from fractions import Fraction
from decimal import Decimal 

ideal_temp = 95.5
current_temp = 95.49999999999999

print(f"ideal temp is {ideal_temp}")
print(f"current temp is {current_temp}")

print(f"difference is {ideal_temp - current_temp}")

print(sys.float_info)

