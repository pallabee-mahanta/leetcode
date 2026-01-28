# binary exponential
def func(mid, n):
    ans = 1
    while n>0:
        if n % 2 == 1:
            ans = ans * mid
            n = n - 1
        else:
            mid = mid * mid
            n = n // 2
    return ans

def nthroot(n, m):
    low, high = 1, m
    while low<=high:
        mid = (low+high)//2
        midN = func(mid, n)
        if midN == m:
            return mid
        elif midN < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 69
print(nthroot(n, m))  # Output: 3