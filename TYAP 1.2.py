import random
n = int(input("Будет загадано число от 1 до: "))
if n>1:
    p = random.randint(1,n)
else:
    p = random.randint(1,100)
    print("Введенная граница некорректна, задано число от 1 до 100")
print("Угадайте число или введите 0 если сдаетесь")
i=0
while i<1:
    a = int(input("Ваше число: "))
    if a == 0:
        print("Вы успешно сдались! Загаданное число: ",p); i=1
    elif a == p:
        print("Вы (наконец-то) угадали число!"); i=1
    else:
        print("Ответ неверный, попробуйте еще раз!")
    
    
        
