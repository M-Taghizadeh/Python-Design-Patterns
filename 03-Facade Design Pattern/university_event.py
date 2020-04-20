# Facade Interface
class EventManager:

    def __init__(self):
        print("Event Manager : Let me coordinate with everyone..")

    def arrange(self):
        self.presenter = Presenter()
        self.presenter.setPresentation()

        self.theaterGroup = TheaterGroup()
        self.theaterGroup.setTheater()

        self.caterer = Caterer()
        self.caterer.setCatering()

        self.lecturer = Lecturer()
        self.lecturer.setLecture()

        self.musicGroup = MusicGroup()
        self.musicGroup.setMusic()

# ------------------------------------------------
# Sub Systems:
class Presenter:

    def __init__(self):
        print("Maraseme shuma che roozi va chand saat ast ? va chand saat ast ? va che noe marasemi ast ?")

    def setPresentation(self):
        print("4 shanbe , 2 saat, jashne voordihaye jadid")


class TheaterGroup:

    def __init__(self):
        print("Theater e tanz bashe ya jedi ?")

    def setTheater(self):
        print("Tanz")


class Caterer:

    def __init__(self):
        print("che paziraee ?")

    def setCatering(self):
        print("keyk, abmiveh, sib")


class Lecturer:

    def __init__(self):
        print("mozoe sokhanrani chieh ? ")

    def setLecture(self):
        print("tafavothaye daneshgah ba dabirestan")


class MusicGroup:
    
    def __init__(self):
        print("chand track ejra konim va az che sabki ?")

    def setMusic(self):
        print("2 track, sonnati")


# ------------------------------------------------
# Client 
class You:

    def __init__(self):
        print("bargozarie jashn niaz be karhaye ziadi darad!")

    def askEventManager(self):
        print("tamame karharo miseparam be anjoman")
        eventmanager = EventManager()
        eventmanager.arrange()

# ------------------------------------------------
# use 
you = You()
you.askEventManager()