def hilbert(n):
    diag = []
    for i in range(n):
        m = 1.0/(2*n - 1)
        diag.append(m)

su = sum(diag)
