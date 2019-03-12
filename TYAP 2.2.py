my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
my_string = my_string.split(';_')
for i in range(0,len(my_string)):
    my_string[i]=my_string[i].split(';') 
print('\t' + my_string[0][0]+my_string[0][1]+my_string[0][2] + '\t\t\t' + my_string[0][3] + '\t\t' + my_string[0][4])
for i in range(1,len(my_string)):
    print(my_string[i][0]+ ' ' + my_string[i][1]+ ' ' + my_string[i][2],'\t\t', my_string[i][3],'\t',my_string[i][4])

