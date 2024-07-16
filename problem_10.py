def transpose(l1, l2):
    for i in range(len(l1[0])):
        row =[]
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2
 
l1 = []
n = int(input("Enter the number of Rows: "))
for _ in range(n):
    l1.append(list(map(int, input().rstrip().split())))

l2 = []
transpose(l1, l2)
print("\n")
for i in l2:
    print(*i)
