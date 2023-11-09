import random

class TTrain:
    def __init__(self, N): #конструктор. Инициализация.
        # в скобках указывааются парамметры, которые передаются при создании объекта этого класса
        #self - передаёт себя
        #Далее поля класса(переменные которые есть у всех объектов данного класса)
        self.wagon = [] #массив словарей
        self.places = 4 #Количество мест в купе
        self.compartment = N #количество купе в вагоне
        self.count_empty = 0 #Счётчик пустых купе
        self.variable = ['м', 'ж', "None"] #варианты значений, которые могут быть в словаре

    #Далее методы(внутренние функции которые можно вызвать у всех объектов данного класса

    def add_value(self): #Метод заполнения массива(передаём в него объект(себя) через self)
        for i in range(self.compartment): #Циклом выполняем действия которые указаны дальше
            #столько раз сколько купе в вагоне
            temp = {} #при каждой итерации цикла сознаём пустой словарь, который олицетворяет купе
            for j in range(1, self.places + 1): #выполняется столько раз, сколько мест в купе
                temp.update({j : random.choice(self.variable)}) #добавляем в словарь пару
                # ключ(номер места в купе) - значение(рандомное из тех, которые могут быть(указаны в поле variable)
            self.wagon.append(temp) #Добавляем в массив полученный словарь

    def serch_empty(self):
        for i in self.wagon:
            print(i)
            flag = True
            for j in i.keys():
                if i[j] != "None":
                    flag = False
                    break
            if flag:
                self.count_empty += 1


# function for task 2.1

# def merge_dict(a, b):
#     return a.update(b)

# first task
# task 1.1
a_set = set([i for i in range(7)])
print(a_set)

# task 1.2
a_set.remove(6)
print(a_set)

upd = [8, 9, 7]

a_set.update(upd)
print(a_set)

# task 1.3
b_set = {11, 12, 3, 4, 5, 6}

# task 1.4
c_set = a_set.difference(b_set)
print(c_set)

# task 1.5
a_dict = {i: i * i for i in range(5)}
print(a_dict)

# metods over dict (task 1.6)

el = a_dict.get(4)
print(el)

item = a_dict.popitem()
print(item)
print(a_dict)

values = a_dict.values()
print(values)

# second task

dict_a = {1: 10,
          2: 20}

dict_b = {3: 30,
          4: 40}

dict_c = {5: 50,
          6: 60}

# merging dicts
res_dict = dict_a | dict_b
res_dict |= dict_c
print(res_dict)

# task 2.2

N = int(input("Введите количество купе: "))
train = TTrain(N)

train.add_value()
train.serch_empty()
print(train.count_empty)
