# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n=int(input('Kол-во элементов первого множества:'))

data1=[]
data2=[]
for i in range(n):
    data1.append(int(input('Введите элемент множества1: ')))
m=int(input('Kол-во элементов второго множества: '))
for i in range(m):
    data2.append(int(input('Введите элемент множества2: ')))
    
print(data1)
print(data2)
print(set(data1).intersection(set(data2)))
