from abc import ABC, abstractmethod

# Abstract class 
class Section(ABC):

    @abstractmethod
    def describe(self):
        pass

# Concrete class
class PersonalInfo_Section(Section):
    def describe(self):
        print("Personal Information Section..")

class Album_Section(Section):
    def describe(self):
        print("Album Section..")

class Patent_Section(Section):
    def describe(self):
        print("Patent Information Section..")


# Abstract Factory Class => Creator
class Profile(ABC):
    sections = []

    def __init__(self):
        self.sections = []
        self.create_profile() # creator method in abc factory => (Factory Method)

    @abstractmethod
    def create_profile(self): 
        pass
    
    def get_sections(self):
        return self.sections

    def add_sections(self, sections):
        self.sections.append(sections)

# Subclasses : LinkedIn and IranianNetwork
class LinkedIn(Profile):

    def create_profile(self):
        self.add_sections(PersonalInfo_Section)
        self.add_sections(Patent_Section)

class IranianNetwork(Profile):

    def create_profile(self):
        self.add_sections(PersonalInfo_Section)
        self.add_sections(Album_Section)

# Client : using Factory Class
if __name__ == "__main__":
    profile_input = input("Select Your Profile for creation : LinkedIn or IranianNetwork\n")
    profile = eval(profile_input)()
    print("Your %s profile created successfuly" %(type(profile).__name__))
    print("Your Sections => [%s]" %(profile.get_sections()))    

    print("\n\nAbout Your Acount sections :")
    sections = profile.get_sections()
    for i in range(len(sections)):
        this_section = eval(sections[i].__name__)()
        this_section.describe()

