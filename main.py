import time

print('Кулинарная книга 1.0')
print('Введите ингридиенты блюда:\n1.Мука\n2.Яйца\n3.Молоко\n4.Масло слив.\n5.Соль\n6.Рис\n7.Cахар\n8.Мясо\n9.Джем') # блюда

dic = [' Хлеб',' Блины',' Тесто',' Лепешки',' Хворост',' Пельмени', ' Паста', ' Плов', 'Чебурек', 'Беляш', 'Равиоли', 'Рис с мясом', 'Гоголь-Моголь', 'Яишница', 
'Вареники с джемом', 'Пирог с джемом', 'Бизе', 'Крем для торта', 'Пирожки с яйцами', 'Запеканка', 'Хинкали', 'Пирог с мясом']
# ингридиенты

while True:
    try:            
        a1 = int(input())
        a2 = int(input())
        a3 = int(input())
        a4 = int(input())
        a5 = int(input())
        a6 = int(input())
        a7 = int(input())
        a8 = int(input())
        a9 = int(input()) 

        if (a1 == 1) and (a2 == 2) and (a3 == 3) and (a4 == 4) and (a5 == 5) and (a6 == 0) and (a7 == 0) and (a8 == 0) and (a9 == 0): # Тесто , Лепешки
            print('Вы получите блюдо : \n' + dic[2], ',\n', dic[3])

        elif (a1 == 1) and (a2 == 2) and (a3 == 3) and (a4 == 4) and (a5 == 5) and (a6 == 0) and (a7 == 7) and (a8 == 0) and (a9 == 0): # Блины, Хворост
            print('Вы получите блюдо : \n' +  dic[1], ',\n', dic[4])

        elif (a1 == 1) and (a2 == 0) and (a3 == 0) and (a4 == 0) and (a5 == 5) and (a6 == 0) and (a7 == 7) and (a8 == 0) and (a9 == 0): # Хворост, Хлеб
            print('Вы получите блюдо : \n' + dic[0], ',\n', + dic[4])

        elif (a1 == 1) and (a2 == 0) and (a3 == 0) and (a4 == 0) and (a5 == 5) and (a6 == 0) and (a7 == 7) and (a8 == 0) and (a9 == 0): # Пельмени, Равиоли
            print('Вы получите блюдо : \n' +  dic[5], ',\n', + dic[10])

        elif (a1 == 1) and (a2 == 2) and (a3 == 3) and (a4 == 0) and (a5 == 5) and (a6 == 6) and (a7 == 0) and (a8 == 8) and (a9 == 0): # Плов, Рис с мясом
            print('Вы получите блюдо : \n' +  dic[7], ',\n', + dic[11])

        elif (a1 == 1) and (a2 == 2) and (a3 == 3) and (a4 == 4) and (a5 == 5) and (a6 == 0) and (a7 == 0) and (a8 == 8) and (a9 == 0): # Чебурек, Беляш
            print('Вы получите блюдо : \n' +  dic[8], ',\n', dic[9])

        elif (a1 == 0) and (a2 == 1) and (a3 == 0) and (a4 == 0) and (a5 == 5) and (a6 == 0) and (a7 == 0) and (a8 == 0) and (a9 == 0): # Гоголь-Моголь, Яишница
            print('Вы получите блюдо : \n' +  dic[12], ',\n', dic[13])

        elif (a1 == 1) and (a2 == 2) and (a3 == 3) and (a4 == 4) and (a5 == 5) and (a6 == 0) and (a7 == 7) and (a8 == 0) and (a9 == 9): # Вареники с джемом, Пирог с джемом
            print('Вы получите блюдо : \n' +  dic[14], ',\n', dic[15])

        elif (a1 == 0) and (a2 == 2) and (a3 == 0) and (a4 == 0) and (a5 == 0) and (a6 == 0) and (a7 == 7) and (a8 == 0) and (a9 == 0): # Бизе, Крем для торта
            print('Вы получите блюдо : \n' +  dic[16], ',\n', dic[17])

        elif (a1 == 1) and (a2 == 2) and (a3 == 0) and (a4 == 4) and (a5 == 5) and (a6 == 0) and (a7 == 7) and (a8 == 0) and (a9 == 0): # Пирожки с яйцами, Запеканка
            print('Вы получите блюдо : \n' +  dic[18], ',\n', dic[19])

        elif (a1 == 1) and (a2 == 2) and (a3 == 0) and (a4 == 0) and (a5 == 5) and (a6 == 0) and (a7 == 0) and (a8 == 8) and (a9 == 0): # Хинкали, Пирог с мясом
            print('Вы получите блюдо : \n' +  dic[20], ',\n', dic[21])

        else:
            print('*** Введите число от 1 до 7 ***')

    except:
        print('*** Вы ввели неправильное значение ***')
    time.sleep(1)


            




