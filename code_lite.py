f = open('first.txt')
n, k = map(int, f.readline().split())
a = []
for i in range(n):
    mat, info, rus, idi, obch = f.readline().split()
    mat, info, rus, idi = int(mat), int(info), int(rus), int(idi)
    a.append([int((mat + info + rus + idi)), int((mat + info + rus)), int(mat), int(info), int(rus), int(idi), obch])
a.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3], -x[4], -x[5], x[6]))
count = 0
count_obch = 0
ob, obc = [], []
for i in range(n):
    count += 1
    if count <= k:
        if a[i][-1] == '+':
            count_obch += 1
            if count_obch <= k * 0.35:
                obc.append(a[i])
            else:
                a[i][-1] = '-'
                ob.append(a[i])
        else:
            ob.append(a[i])
        if count == k:
            print(a[i][3])
x = 0
for i in range(len(obc)):
    x += obc[i][0]
print(x/len(obc))

