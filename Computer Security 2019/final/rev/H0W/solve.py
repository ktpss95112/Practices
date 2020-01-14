import time
from pwn import *

def c_PRNG(seed):
    # reference: https://www.mscs.dal.ca/~selinger/random/
    r = [ _ for _ in range(344) ]
    r[0] = seed
    for i in range(1, 31):
        r[i] = (16807 * r[i-1]) % 2147483647
    for i in range(31, 34):
        r[i] = r[i-31]
    for i in range(34, 344):
        r[i] = (r[i-31] + r[i-3]) % 4294967296
    i = 344
    while True:
        r[i%344] = (r[(i-31+344)%344] + r[(i-3+344)%344]) % 4294967296
        yield (r[i%344] >> 1)
        i += 1


debug = True


if debug:
    f = open('output.txt', 'rb').read()[-56:]
else:
    f = open('original_output.txt', 'rb').read()[-56:]
data = f.decode('ascii').replace('\x00', '')
print(data)
out_tm_year = int(data[:4])
out_tm_mon = int(data[4:6]) + 1
out_tm_wday = (int(data[6:8]) - 1 + 7) % 7
out_tm_hour = int(data[8:10])
out_tm_min = int(data[10:12])
out_tm_sec = int(data[12:14])
print(out_tm_year, out_tm_mon, out_tm_wday, out_tm_hour, out_tm_min, out_tm_sec)
# 2019 08 03 05 25 14
# /* The number of years since 1900*/ /* month, range 0 to 11*/ /* day of the week, range 0 to 6*/ /* hours, range 0 to 23*/ /* minutes, range 0 to 59*/ /* seconds,  range 0 to 59*/

def leftRotate(n, d):
    return (n << d)|(n >> (32 - d))

def rightRotate(n, d):
    return (n >> d)|(n << (32 - d)) & 0xFFFFFFFF

def ichi_rev(x):
    return x ^ 0xfaceb00c

def ni_rev(x):
    return (x - 0x12384 + (2**32)) % (2**32)

def san_rev(x):
    return (rightRotate((x & 0xaaaaaaaa), 2) | leftRotate((x & 0x55555555), 4)) % (2**32)

def yon_rev(x):
    return ichi_rev(ni_rev(san_rev(x)))


if not debug:
    bound = [1578739178-10000, 1578739178+100000]
else:
    bound = [1565000000, 1570800000]
for t in range(*bound):
    tm = time.gmtime(t)
    if tm.tm_year == out_tm_year and tm.tm_mon == out_tm_mon and tm.tm_wday == out_tm_wday and tm.tm_hour == out_tm_hour and tm.tm_min == out_tm_min and tm.tm_sec == out_tm_sec:
        print(t, tm)
    else:
        continue
    
    dec_file = open(f'dec_{t}.txt', 'wb')
    if debug:
        data = open('output.txt', 'rb').read()[:-56]
    else:
        data = open('original_output.txt', 'rb').read()[:-56]
    
    assert len(data) % 4 == 0
    c_rand = c_PRNG(t)

    for i in range(0, len(data), 4):
        if data[i:i+4] == b'\x00\x00\x00\x00':
            print(b'\x00\x00\x00\x00')

        func = [ichi_rev, ni_rev, san_rev, yon_rev][next(c_rand)%4]
        dec_file.write(p32(func(u32(data[i:i+4]))))
        # print(p32(func(u32(data[i:i+4]))))

    dec_file.close()




