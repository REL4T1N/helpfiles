f = open('third.txt', 'r', encoding='utf-8')
n, k = map(int, f.readline().split())
bvi, os, ot, cel, kon = [], [], [], [], []
a = []
for i in range(n):
    mat, info, rus, idi, st = map(int, f.readline().split())
    a.append([mat+info+rus+idi, mat+info+rus, mat, info, rus, idi, st])

a.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3], -x[4], x[5], x[-1]))
for i in range(n):
    ks, s, mat, info, rus, idi, st = a[i]
    if st == 1:
        bvi.append([300+idi, 300, 100, 100, 100, idi, st])
    if st == 2 and len(os) < k * 0.1:
        os.append([ks, s, mat, info, rus, idi, st])
    elif st == 2 and len(os) >= k * 0.1:
        kon.append([ks, s, mat, info, rus, idi, 5])
    if st == 3 and len(ot) < k * 0.1:
        ot.append([ks, s, mat, info, rus, idi, st])
    elif st == 3 and len(ot) >= k * 0.1:
        kon.append([ks, s, mat, info, rus, idi, 5])
    if st == 4:
        cel.append([ks, s, mat, info, rus, idi, st])
    if st == 5:
        kon.append([ks, s, mat, info, rus, idi, st])

bvi.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3], -x[4], x[5], x[-1]))
os.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3], -x[4], x[5], x[-1]))
ot.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3], -x[4], x[5], x[-1]))
cel.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3], -x[4], x[5], x[-1]))
kon.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3], -x[4], x[5], x[-1]))
postupi = []
lst = 0
for i in range(len(bvi)):
    if len(postupi) < k:
        postupi.append(bvi[i])
for i in range(len(os)):
    if len(postupi) < k:
        postupi.append(os[i])
for i in range(len(ot)):
    if len(postupi) < k:
        postupi.append(ot[i])
for i in range(len(cel)):
    if len(postupi) < k:
        postupi.append(cel[i])
for i in range(len(kon)):
    if len(postupi) < k:
        postupi.append(kon[i])
        lst = i+1

max_neproxod = kon[lst][1]
summ = 0
summprof = 0
for i in range(k):
    summ += postupi[i][0]
    if postupi[i][-1] in [2, 3, 4] and postupi[i][1] > max_neproxod:
        summprof += postupi[i][2] + postupi[i][3]

srsumm = summ / k
count = 0
for i in range(k):
    if postupi[i][0] >= 5 + srsumm:
        count += 1

print(count, summprof)







