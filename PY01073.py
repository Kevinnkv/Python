# HOÁN VỊ KÝ TỰ

import itertools
s = input()
p = itertools.permutations(s)
for i in p:
    print(''.join(i))
