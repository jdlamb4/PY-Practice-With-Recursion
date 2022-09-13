def trib(n):
    if n <= 2:
        return max(n-1, 0)
    else:
        return trib(n-1) + trib(n-2) + trib(n-3)

print(trib(7))

# 0 0 1 1 2 4
# 0 1 2 3 4 5
