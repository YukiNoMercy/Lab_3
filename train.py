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
