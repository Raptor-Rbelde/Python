### Modules ###

#import my_module

#my_module.sum(1, 3, 5)
#my_module.tablas(10)

from my_module import tablas
from my_module import sum

tablas(11)
sum(10, 4, 8)

import math
from math import pi as pi_value

print(math.pi)
print(int(math.pow(10, 2)))
print(pi_value)