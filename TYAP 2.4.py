n = int(input("Введите число элементов списка (>10): "))
p = []
for i in range(0,n):
    p.append(int(input('Введите ' + str(i+1) + ' элемент: ')))
print(p)
p = [x for x in p if x % 2 != 0]
p.append(int(input('Введите два новых элемента:\n1) ')))
p.append(int(input('2) ')))
print(p)    
