n =  int(input())
a = list(map(int, input().split()))
for i in range(n-1) :
    a.sort()
print(a[0])