h, b, c, s = map(int, input().split())
r = (h * b * c * s * 1/8/1024/1024)
print(format(r, '.1f'), 'MB')