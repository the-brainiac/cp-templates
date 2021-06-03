import math
def generate_segment(arr):
    n = len(arr)
    n = 2**math.ceil(math.log2(n))
    seg = [0]*(2*n)
    for i in range(len(arr)):
        seg[n+i] = arr[i]
    for k in range(n-1, 0, -1):
        seg[k] = seg[2*k] + seg[2*k+1]
    
    return seg

def update(idx, val):
    n = 2**math.ceil(math.log2(len(arr)))
    idx += n
    seg[idx] = val
    idx //= 2
    while idx > 0:
        seg[idx] = seg[2*idx] + seg[2*idx + 1]
        idx //= 2


def query(a, b):
    n = 2**math.ceil(math.log2(len(arr)))
    a += n
    b += n
    res = 0
    while a <= b:
        if a%2:
            res += seg[a]
            a += 1
        if b%2 == 0:
            res += seg[b]
            b -= 1
        a //= 2
        b //= 2

    return res



if __name__ == '__main__':
    arr = list(map(int, input().split()))
    seg = generate_segment(arr)
    print(seg)
    update(1, 5)
    print(query(1, 7))
