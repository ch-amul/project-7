#priavte variable
##class robot(object):
##    def __init__(self):
##        self.__version = 22
##
##    def getversion(self):
##        print(self.__version)
##
##    def setversion(self, version):
##        self.__version = version
##
##
##
##obj = robot()
##obj.getversion()
##obj.setversion(23)
##obj.getversion()




#private method

class car:

     def __init__(self):
         self.__updateSoftware()

     def drive(self):
        print('driving')

     def __updateSoftware(self):
        print('updating software')

redcar = car()
redcar.drive()
#if u call private method from outside the class it wont give output unless it i sin te constructor as done in th e above program.










