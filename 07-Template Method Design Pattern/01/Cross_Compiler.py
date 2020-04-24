from abc import ABC, abstractmethod

# Abstract Base Class
class Compiler(ABC):

    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass
    
    @abstractmethod
    def run(self):
        pass

    # Template Method => Defines algorithm with calling operation methods
    def compile_and_run(self):
        self.collectSource()
        self.compileToObject()
        self.run()

# Concrete Class:
class IOS_Compiler(Compiler):

    def collectSource(self):
        print("Collecting Source Code..")

    def compileToObject(self):
        print("Compiling source code to binary code..")

    def run(self):
        print("Compiler is running..")

# Client 
# Use
ios_compiler = IOS_Compiler()
ios_compiler.compile_and_run() 