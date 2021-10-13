class Tomato:

    stages = {1: 'non', 2: 'bloom', 3: 'green', 4: 'red'}

    def __init__(self, index, stage=1):
        self.index = index
        self.stage = stage

    def growth(self):
        if self.stage < 4:
            self.stage += 1
        return self.stage

    def display_stage(self):
        return Tomato.stages[self.stage]


class TomatoBush:
    def __init__(self, tomato_number):
        self.tomato_list = [Tomato(i) for i in range(tomato_number)]

    def growth_bush(self):
        for tomato in self.tomato_list:
            tomato.growth()
        print('Куст растет')

    def display_bush(self):
        self.stage1 = self.tomato_list[0].display_stage()
        for tomato in self.tomato_list:
            print(f'Помидор {tomato.index} имеет стадию зрелости {tomato.stage}')

    def all_red_tomatos(self):
        for i in self.tomato_list:
            if i.stage == 4:
                return True
            else:
                return False

    def harvesting(self):
        self.tomato_list.clear()


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def plant_care(self):
        self.plant.growth_bush()

    def caring(self):
        print('Садовник ухаживает')

    def get_tomatos(self):
        if self.plant.all_red_tomatos():
            self.plant.harvesting()
            print('Все помидоры собраны')
        else:
            print('Не все помидоры дозрели')


tb = TomatoBush(3)
tb.growth_bush()
tb.display_bush()
print(tb.all_red_tomatos())
# tb.harvesting()


g = Gardener('Vova', tb)
g.plant_care()
g.plant_care()
g.plant_care()
g.plant_care()
tb.display_bush()


# g.caring()
g.get_tomatos()













































