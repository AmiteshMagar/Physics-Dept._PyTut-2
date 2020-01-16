def arrayMani():
    n = int(input("Enter the number of elements in the array\n"))
    ls = []
    for i in range(n):
        ls.append(float(input()))
    mx = max(ls)
    mn = min(ls)
    avg = sum(ls)/n
    return mx,mn,avg

print(arrayMani())
