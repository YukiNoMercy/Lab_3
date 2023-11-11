import random

class TTrain:
    def __init__(self, N): #конструктор. Инициализация класса. Обязательно надо.
        # в скобках указывааются парамметры, которые передаются при создании объекта этого класса
        #self - передаёт себя
        #Далее поля класса(переменные которые есть у всех объектов данного класса)
        self.wagon = [] #массив словарей
        self.places = 4 #Количество мест в купе
        self.compartment = N #количество купе в вагоне
        self.count_empty = 0 #Счётчик пустых купе
        self.indexs = []
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

    def serch_empty(self): #Метод для поиска пустых купе
        j = 0
        for i in self.wagon: # Цикл, который перебирает элементы массива(То есть мы в и храним словарь(купе))
            j += 1
            print(i) #просто выводим текущий словарь(купе)
            flag = True #Переменная в которой мы храним булево(логическое значение)
            #ее мы будем использовать для того чтобы понять, пустое купе или нет
            for j in i.keys(): #Циклом перебираем ключи словаря(уникальные значения)(в данном случае места в купе от 1 до 4)
                if i[j] != "None": # Проверяем значение, которое соответствует ключу
                    # Если у нас значение не равно "None" то есть место занято, то в
                    # переменную flag сохраняем false - то есть купе не пустое и с помощью break досрочно выходим из цикла,
                    # чтобы он не проверял лишние значение. это убыстряет работу программы
                    flag = False
                    break
            if flag: #Если у нас в переменной flag лежит True, То мы увеличиваем значение переменной,
                # которая отвечает за подсчёт пустых вагонов на 1
                self.count_empty += 1
                self.indexs.append(j)



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
a_dict = dict([["1", 1], ["2", 4], ["3", 9], ["4", 16]])
# a_dict = {i: i * i for i in range(5)}
print(a_dict)

# metods over dict (task 1.6)

el = a_dict.get("4")
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
train = TTrain(N) # Создаём объект train, класса TTrain(или же типа)

#дальше вызываем методы у объекта и после выводим знаечение поля count_empty
train.add_value()
train.serch_empty()
print(train.count_empty)
print(train.indexs)
