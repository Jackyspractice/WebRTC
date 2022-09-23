

from tkinter.messagebox import NO


SG90_Degree = []

class SG90:

    def __init__(self, degree = None, duty = None, frequence = None) -> None:

        self.degree = degree
        self.duty = duty
        self.frequence = 50 #50Hz

    def Set_degree_argument(self):
        
        SG90_Degree.clear()

        Degree_0 = SG90()
        Degree_0.degree = 0
        Degree_0.duty = 2.5
        SG90_Degree.append(Degree_0)

        Degree_45 = SG90()
        Degree_45.degree = 45
        Degree_45.duty = 5
        SG90_Degree.append(Degree_45)

        Degree_90 = SG90()
        Degree_90.degree = 90
        Degree_90.duty = 7.5
        SG90_Degree.append(Degree_90)

        Degree_135 = SG90()
        Degree_135.degree = 135
        Degree_135.duty = 10
        SG90_Degree.append(Degree_135)

        Degree_180 = SG90()
        Degree_180.degree = 180
        Degree_180.duty = 12.5
        SG90_Degree.append(Degree_180)


test = SG90()

test.Set_degree_argument()

for i in range (0, len(SG90_Degree)):

    print(SG90_Degree[i].frequence)
