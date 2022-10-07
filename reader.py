file = open("test1.dat", "r")
spisok = []
spisoklines = file.readlines() #список из строк файла
for i in range (1, len(spisoklines)): # список из строк нарезается на отедльные числа
    a = spisoklines[i-1].split(  )
    for k in range (1, len(a)):
        spisok.append(a[k])
print(spisok)
for i in range (0, len(spisok)):
    spisok[i]=float(spisok[i]) #команда int почему-то не работала

print(spisok) #пузырьковая сортировка
for k in range(1, len(spisok)):
    for i in range(1, len(spisok)):
        if spisok[i - 1] > spisok[i]:
            a = spisok[i]
            spisok[i] = spisok[i - 1]
            spisok[i - 1] = a
print(spisok)