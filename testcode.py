
import os
dir = os.path.abspath('.')
file = os.path.join(dir, 'tests\\sample2.py')
fd = open(file, 'r+')
strings = fd.read()


files = {
    'sample2.py':strings}

from pyblade import scan

res = scan(files)
print res
