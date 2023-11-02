#function for task 2.1

# def merge_dict(a, b):
#     return a.update(b)

#first task
#task 1.1
a_set = set([i for i in range(7)])
print(a_set)

#task 1.2
a_set.remove(6)
print(a_set)

upd = [8, 9, 7]

a_set.update(upd)
print(a_set)

#task 1.3
b_set = {11, 12, 3, 4, 5, 6}

#task 1.4
c_set = a_set.difference(b_set)
print(c_set)

#task 1.5
a_dict = {i: i * i for i in range(5)}
print(a_dict)

#metods over dict (task 1.6)

el = a_dict.get(4)
print(el)

item = a_dict.popitem()
print(item)
print(a_dict)

values = a_dict.values()
print(values)

#second task

dict_a = {1: 10,
          2: 20}

dict_b = {3: 30,
          4: 40}

dict_c = {5: 50,
          6: 60}

#merging dicts
res_dict = dict_a | dict_b
res_dict |= dict_c
print(res_dict)