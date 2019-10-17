from collections import defaultdict
import json

class Item(object):
    def __init__(self):
        self.materials = []
        self.raw_materials = []

    def __str__(self):
        return self.__class__.__name__

    def get_raw_materials(self):
        return self.__get_raw_materials(-1, [], defaultdict(list), 0)

    def __get_raw_materials(self, level, raw_materials_list, all_materials_dict, time):
        level += 1
        for mat in self.materials:
            if type(mat) == str:
                raw_materials_list.append(mat)
            elif type(mat) == int:
                raw_materials_list.append(mat)
                time += mat
            else:
                all_materials_dict[level].append(str(mat))
                raw_materials_list, all_materials_dict, time = mat.__get_raw_materials(level, raw_materials_list, all_materials_dict, time)
        return raw_materials_list, all_materials_dict, time

class CopperOre(Item):
    def __init__(self):
        super().__init__()
        self.materials = ['CopperOre']

class IronOre(Item):
    def __init__(self):
        super().__init__()
        self.materials = ['IronOre']

class CopperPlate(Item):
    def __init__(self):
        super().__init__()
        self.materials = [CopperOre()]

class IronPlate(Item):
    def __init__(self):
        super().__init__()
        self.materials = [IronOre(), Time(3)]

class IronGearWheel(Item):
    def __init__(self):
        super().__init__()
        self.materials = [IronPlate(), IronPlate(), Time(5)]

class AutomationSciencePack(Item):
    def __init__(self):
        super().__init__()
        self.materials = [IronGearWheel(), CopperPlate(), Time(10)]

class Time(Item):
    def __init__(self, seconds):
        super().__init__()
        self.materials = [seconds]

    def __str__(self):
        return f"{self.__class__.__name__}: {' '.join(map(str, self.materials))} seconds"

if __name__ == '__main__':
    science = AutomationSciencePack()
    raw_materials = defaultdict(int)
    all_materials = science.get_raw_materials()[1]
    time = science.get_raw_materials()[2]
    for i in science.get_raw_materials()[0]:
        raw_materials[i] += 1

    print(json.dumps(raw_materials, indent=4))
    print(json.dumps(all_materials, indent=4))
    print(f'Total Time: {time} seconds')
    # for i in all_materials:
    #     print(i)