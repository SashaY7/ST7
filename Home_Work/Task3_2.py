#Знайти добуток цифр числа
n = 1234
Dobutok = 1*2*3*4
print ("Dobutok", Dobutok)
#Записати число в реверсному порядку

#n1 = 1234
#n2 = n1[::-1]
#print ("Реверсне число: ", n2)

n1 = 1234
n_list = list(str(n1))
n_list.reverse()
n2 = "".join(n_list)
print('"Реверсне число:', n2)

#сортування чисел
n1 = 6787
n2 = str(n1)
print ("n2: ", sorted(n2))
print (int(n2))