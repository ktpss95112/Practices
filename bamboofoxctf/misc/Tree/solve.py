import os

def dfs(dirPath):
    files = os.listdir(dirPath)
    num_0, num_1 = 0, 0
    if '0_number' in files:
        num_0 = int(open(os.path.join(dirPath, '0_number'), 'r').read())
        # print(os.path.join(dirPath, '0_number'), ':', num_0)
    else:
        dirName = '0_+' if '0_+' in files else '0_x'
        num_0 = dfs(os.path.join(dirPath, dirName))

    if dirPath[-1] == ']': return num_0

    if '1_number' in files:
        num_1 = int(open(os.path.join(dirPath, '1_number'), 'r').read())
        # print(os.path.join(dirPath, '1_number'), ':', num_1)
    else:
        dirName = '1_+' if '1_+' in files else '1_x'
        num_1 = dfs(os.path.join(dirPath, dirName))
    

    operator = '*' if dirPath[-1] == 'x' else '+'
    return eval('num_0' + operator + 'num_1')

for i in range(37):
    print(chr(dfs(f'flag[{i}]')), end='')
print()
