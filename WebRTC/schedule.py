class Box(object):
    def __init__(self, name = None, days = 7):
        self.name = name
        self.weekday = [days]
class Person(object):
    def __init__(self):
        self.name = None
        self.weekday = [7]
class Weekday(object):
    def __init__(self, name = None, box = None):
        self.name = name
        self.box = box

All_Box = [None] * 6
All_Weekday = [None] * 7
All_Person = []

class store:

    def Box(name, weekday):
        Box_tmp = Box()
        Box_tmp.name = name
        Box_tmp.weekday = weekday

        return Box_tmp

    def Weekday(name, box):
        Weekday_tmp = Weekday()
        Weekday_tmp.name = name
        Weekday_tmp.box = box

        return Weekday_tmp

    def Person(name, weekday, box):
        person_tmp = Person()
        person_tmp.name = name
        person_tmp.weekday[weekday - 1] = box

        return person_tmp

class set_schedule:

    def write_to_file(self):
        print()
        
    def set(self, name, weekday, box):

        All_Box[box - 1] = store.Box(name, weekday)
        All_Weekday[weekday - 1] = store.Weekday(name, box)
        All_Person.append(store.Person(name, weekday, box))

if __name__ == "__main__":

    set = set_schedule()
    set.set("jacky", 1, 6)

    print(All_Person[0].name)
    print("Box number = " + str(All_Person[0].weekday[0]))

    print(All_Box[5].name)
    print(All_Box[5].weekday)

    print(All_Weekday[0].name)
    print(All_Weekday[0].box)