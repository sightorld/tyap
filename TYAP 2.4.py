n = int(input("Введите число элементов списка (>10): "))
p = []
for i in range(0,n):
    p.append(input('Введите ' + str(i+1) + ' элемент: '))
print(p)
i = 0; b = 0
while i < n - b:
    if int(p[i]) % 2 == 0:
        p.remove(p[i])
        b = b+1
        i = i - 1
    i = i+1
p.append(input('Введите два новых элемента:\n1) '))
p.append(input('2) '))
print(p)    
