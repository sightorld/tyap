my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
p = my_string.split(';_')
for i in range(0,len(p)):
    p[i] = p[i].split(';')
    if i == 0:
        print((p[i][0] + p[i][1] + p[i][2]).ljust(25),p[i][3].ljust(8),p[i][4])
    else:
        print((p[i][0]+' '+ p[i][1]+' '+p[i][2]).ljust(25),p[i][3].ljust(8),p[i][4])

