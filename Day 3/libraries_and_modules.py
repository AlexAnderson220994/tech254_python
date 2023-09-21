# Libraries and Modules

# Python has very extensive libraries and modules, this is great for us as DevOps engineers!

# Module = single file of functions, classes, variables etc. that you can bring in and use in another Python file.

# Library = Collection of modules. Needs to be installed with pip (python package/module manager)

import math
import random
import requests


# num_float = 23.66
#
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)

request_bbc = requests.get("https://www.bbc.co.uk")

print(request_bbc.status_code)
print(request_bbc.content)
