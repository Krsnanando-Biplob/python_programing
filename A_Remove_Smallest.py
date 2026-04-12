
t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    if max(a) - min(a) <= 1:
        print("YES")
    else:
        print("NO")