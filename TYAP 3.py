import os, os.path

def zad1():
    dic = os.listdir(input("\nВведите директорию:\n\n - ")) 
    print("\nВ данной папке",len([name for name in dic if os.path.isfile(name)]),"файлов")

def zad2(p, temp):
    with open("products.txt",'r') as prod:    
        for line in prod:
            temp.append(line.rstrip()) #запись каждой строки как элемент списка без \n
        for i in range(0,len(temp)):
            temp[i] = temp[i].split(';') #деление каждого элемента на список
    p.append(temp[0])                                       #добавление заголовочного списка в конечный список
    temp.remove(temp[0])                                    #удаление заголовка из временного
    temp.sort(key=lambda temp:int(temp[2]))                 #сортировка временного по int
    p.extend(temp)                                          #добавление отсортированного в конечный
    print("\nОтсортированный список товаров:\n")
    for i in range(0,len(p)):
        print(p[i][0].ljust(3),p[i][1].ljust(20),p[i][2].ljust(6),p[i][3].ljust(3)) #вывод
    return p, temp

def zad3(p ,temp):
    s = input("\nВведите номера товаров, которые Вы хотели бы уменьшить в кол-ве через пробел:\n\n - ")
    s = s.split()
    s = [int(i) for i in s if i.isdigit()]
    s = [i for i in s if i>0 and i<len(p)] 
    n = int(input("\nНа сколько бы вы хотели уменьшить их кол-во?\n\n - "))
    temp.sort() #обратная сортировка, номер товара совпадает с индексом в списке   
    for i in range(0,len(s)):
        temp[s[i]-1][3] = str(int(temp[s[i]-1][3]) - n)
        if  int(temp[s[i]-1][3]) < 0:
            temp[s[i]-1][3] = '0'
    temp.sort(key=lambda temp:int(temp[2])) #сортируем обратно, делаем конечный список
    p = [p[0]]
    p.extend(temp)
    print("\nСписок с обновленным кол-вом товаров:\n")
    for i in range(0,len(p)):
        print(p[i][0].ljust(3),p[i][1].ljust(20),p[i][2].ljust(6),p[i][3].ljust(3))
    return p, temp

def zad4(p, temp):
    n = input('''\n\nКак бы вы хотели сохранить отсортированный список?
1) В тот же файл
2) В отдельный файл (будет создан в той же папке)

 - ''')
    if int(n) == 1:
        with open("products.txt",'w') as prod:
            for i in range(0,len(p)):
                prod.write(p[i][0]+';'+p[i][1]+';'+p[i][2]+';'+p[i][3]+'\n')
        print("\nФайл успешно перезаписан!")
    elif int(n) == 2:
        with open('newlist.txt','w') as prod:
            for i in range(0,len(p)):
                prod.write(p[i][0]+';'+p[i][1]+';'+p[i][2]+';'+p[i][3]+'\n')
        print("\nФайл newlist.txt успешно создан!")
    else:
        print("\nНекорректный ввод, принудительное завершение без сохранения")
    return p, temp
    
k = int(input('''Выберите действие:

0 - Выход из программы
1 - Подсчет файлов в заданной директории
2 - Сортировка товаров из products.txt по цене
3 - Та же сортировка (2) + уменьшение кол-ва на заданное число
4 - (3) + сохранение изменений

 - '''))

while k != 0:
    temp = [] #временный список, для начальной записи и последующей сортировки
    p = []
    if k == 1:
        zad1()    
    elif k in {2,3,4}:
        p, temp = zad2(p, temp)
        if k in {3,4}:
            p, temp = zad3(p, temp)
            if k == 4:
                p, temp = zad4(p, temp)
    else:
        k = int(input("Введите корректный номер действия:\n\n - "))

    q = input("\nВы хотите продолжить? (Y, yes, 1 // N, no, 0)\n\n - ")
    if q in {'Y','yes','1'}:
        k = int(input("\nВыберите действие из изначального списка:\n\n - "))
    elif q in {'N','no','0'}:
        k = 0
    else:
        print("Некорректный ввод, принудительное завершение работы программы")
        k = 0             
print("\nСпасибо за использование данной программы!")        

