f = open('test1.txt')
n, k = map(int, f.readline().split())

a = []
for i in range(n):
    b, r, at = f.readline().split()
    # b, r, at = b[i]
    a.append([int(b), int(r), at])

a.sort(key=lambda x: (-x[0], x[1]))
count = 0
last = []
for i in range(n-1):
    b, r, at = a[i]
    if r == 1 and at == '+':
        count += 1
        krilov = count + ((i + 1) / 5)
        if krilov <= k:
            last = [i+1] + a[i]

kol, bal = 0, 0
for i in range(n):
    if [i+1] + a[i] == last:
        break
    else:
        bal += a[i][0]
        kol += 1
print(last[0], bal/kol)

# тут хитрость в том, что абитуриентов с 1-ым приоритетом и 215 баллами несколько и не все они проходят по формуле
# Крылова, поэтому необходимо запоминать их место в общем списке
# a = []
# for i in range(n):
#     b_val, r, at = f.readline().split()
#     a.append([int(b_val), int(r), at])

a.sort(key=lambda x: (-x[0], x[1]))
count = 0
last = []
for i in range(n):
    b_val, r, at = a[i]
    if r == 1 and at == '+':
        count += 1
        krilov = count + ((i + 1) / 5)
        if krilov <= k:
            last = [i+1] + a[i]

kol, bal = 0, 0
for i in range(n):
    if [i+1] + a[i] == last:
        break
    else:
        bal += a[i][0]
        kol += 1
print(last[0], bal/kol)