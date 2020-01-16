n = int(input("Enter the number of elements in the row matrix\n"))
rowM = []
for i in range(n):
    rowM.append(float(input()))

def descSort(ls):
    l = len(ls)
    for i in range(l):
        for  j in range(i,l):
            if ls[i]<ls[j]:
                ls[i],ls[j]=ls[j],ls[i]
    return ls

print(descSort(rowM))
        
