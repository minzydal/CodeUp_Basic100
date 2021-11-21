w, b, h = map(int, input().split())
print(format(w * b * h / 8 / 1024 / 1024, '.2f'), 'MB')