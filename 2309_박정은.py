import itertools

n = []
for i in range(9):
    num = int(input())
    n.append(num)


for i in itertools.combinations(n, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break;
