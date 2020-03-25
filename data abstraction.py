class justcounter:
    __secretcount = 0


    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)

counter = justcounter()
counter.count()
for i in range(5):
    counter.count()
#we can write either the loop 
