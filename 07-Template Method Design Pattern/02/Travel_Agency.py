from abc import ABC, abstractmethod
# ---------------------------------
# Abstract class
class Travel(ABC):

    @abstractmethod
    def day1(self):
        pass 

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def return_from_travel(self):
        pass
    
    # Template Method => Defines algorithm with calling operation methods
    def travel_plan(self):
        self.day1()
        self.day2()
        self.day3()
        self.return_from_travel()

# ---------------------------------
# Concrete Classes => 1:ShirazTour, 2:EsfahanTour
class ShirazTour(Travel):
    
    def day1(self):
        print("Takhte Jamshid")

    def day2(self):
        print("Shah Cheragh")

    def day3(self):
        print("Hafezieh and Baghe eram")

    def return_from_travel(self):
        print("Return From Shiraz Tour")


class EsfahanTour(Travel):
    
    def day1(self):
        print("33 Pol")

    def day2(self):
        print("Meydane naghshe jahan")

    def day3(self):
        print("40 Sotoon and Pole khajo")

    def return_from_travel(self):
        print("Return From Esfahan Tour")

# ---------------------------------
# Client
class Travel_Agency:

    def make_travel(self):
        maghsad = input("Select the city number for traveling\n1:Shiraz\n2:Esfahan\n")

        if maghsad == "1":
            self.safar = ShirazTour()
            self.safar.travel_plan()

        elif maghsad == "2":
            self.safar = EsfahanTour()
            self.safar.travel_plan()

# Use
travel_agency = Travel_Agency()
travel_agency.make_travel()
