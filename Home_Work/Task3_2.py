#Знайти добуток цифр числа
import math
numbers = (7, 8, 9)
print("Prod numbers: ", math.prod(numbers))


#Записати число в реверсному порядку

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