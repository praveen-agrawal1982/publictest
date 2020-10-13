import json
import os

print("Greetings")

import sys
import os
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(os.getenv('name'))
print(os.getenv('CDAL_host'))

print(os.getenv('HYPERPARAM_PATH'))
f = open(os.getenv('HYPERPARAM_PATH'),)
data = json.load(f)
print(data['C'])
f.close()
