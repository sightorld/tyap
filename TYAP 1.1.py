a = int(input("Ввод A: "))
b = int(input("Ввод B: "))
c = int(input("Ввод C: "))
d = int(input("Ввод D: "))
k = int(input("Ввод K: "))
if b==0 or a==0:
    print("Произошло деление на ноль :^(")
else:
    print(abs(( (a**2 - b**3 - c**3 * a**2) * (b - c + c * (k-d/b**3)) - ((k/b - k/a)*c))**2 - 20000))
 
