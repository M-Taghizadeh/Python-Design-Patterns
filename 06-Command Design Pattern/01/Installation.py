# Command Class
class Installer:

    def __init__(self, source_folder, installation_folder):
        self.choices = [] # each choce is a dict
        self.source_folder = source_folder
        self.installation_folder = installation_folder
    
    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying", self.source_folder, "into", self.installation_folder)
            else:
                print("No action was performed")

# Use
if __name__ == "__main__":
    installer = Installer("python", "D:/python")
    installer.preferences({"python": True})
    installer.preferences({"java": False})
    installer.execute()