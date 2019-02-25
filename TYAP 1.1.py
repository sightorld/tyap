a = int(input("Ввод A: "))
b = int(input("Ввод B: "))
c = int(input("Ввод C: "))
d = int(input("Ввод D: "))
k = int(input("Ввод K: "))
if b==0 or a==0:
    print("Произошло деление на ноль :^(")
else:
    res = (pow(a,2)-pow(b,3)-(pow(c,3)*pow(a,2)))*(b-c+c*(k-(d/pow(b,3))))-pow((k/b-k/a)*c,2)-20000
    if res<0: res=-res
    print(res)   
