import numpy as np

pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz'
values = [ 185, 212, 172, 145, 185, 212, 172, 177, 217, 212, 204, 177, 185, 212, 204, 209, 161, 124, 172, 177 ]

for c in map(ord, pool):
    x = [c]
    for i in range(19):
        x.append( values[i] - x[-1] )

    print(''.join(map(chr, x)))

# FLAG{PikAPikApikaPikap1Ka}

