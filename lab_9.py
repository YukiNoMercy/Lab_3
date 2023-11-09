import random


class TTrain:
    def __init__(self, N):
        self.wagon = []
        self.places = 4
        self.compartment = N
        self.count_empty = 0
        self.variable = ['м', 'ж', "None"]

    def add_value(self):
        for i in range(self.compartment):
            temp = {}
            for j in range(1, self.places + 1):
                temp.update({j : random.choice(self.variable)})
            self.wagon.append(temp)

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
