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

    def All(self):
        data = "All Schedule\n(Name, Weekday, Box)\n"
        file = open("schedule.txt", "r")
        
        lines = file.readlines()

        for l in lines:
            data += l
        #data = lines.split("\n")

        file.close()

        return data + "-END of List-"

    def find_all_people(self):
        names = []
        names.clear()

        file = open("member.txt", "r")
        line = file.readline()
        names = line.split(",")

        file.close()
        return names

    def find_person_box(self, name):
        person_data = []
        person_data.clear()
        file = open("schedule.txt", "r")
        lines = file.readlines()
        file.close()

        index = 0
        for line in lines:
            index += 1
            temp = line
            line = line.split(",")
            if (line[0] == name):
                person_data.append(temp)

        return person_data
        
    def delete_person(self, name):
        write_data = []
        write_data.clear()
        file = open("schedule.txt", "r")
        lines = file.readlines()
        file.close()

        index = 0
        for line in lines:
            index += 1
            temp = line
            line = line.split(",")
            if (line[0] != name):
                write_data.append(temp)

        
        if (len(write_data) == index):
            return "Person doesn't exist!"

        file = open("schedule.txt", "w")
        for data in write_data:
            file.write(data)
        file.close()

        write_data.clear()
        return "delete successfully!"

    def write_to_file(self, name, weekday, box):
        file = open("schedule.txt", "a")
        file.write(str(name) + "," + str(weekday) + "," + str(box) + "\n")
        file.close()
        return "add successfully!"
        
    def set(self, name, weekday, box):

        #All_Box[box - 1] = store.Box(name, weekday)
        #All_Weekday[weekday - 1] = store.Weekday(name, box)
        #All_Person.append(store.Person(name, weekday, box))

        return self.write_to_file(name, weekday, box)

if __name__ == "__main__":

    set = set_schedule()
    #set.set("jacky", 1, 6)
    #set.set("tim", 2, 3)


    #set.delete_person("tim")

    print("found")
    list = set.find_all_people()
    print("list len = ", len(list))
    for name in list:
        print(name)

    data = set.All()
    print(data)