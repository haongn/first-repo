# handling missing keys with setdefault method 
# we show that dict.get is not the best way to handle a missing key.

import sys
import re 


WORD_RE = re.compile('w+')

index = {}
with open(sys.argv[1], encoding = 'utf8') as fp: 
    for line_no, line in enumerate(fp, 1): 
        


