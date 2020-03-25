##class parent():
##    def __init__(self):
##        self.value = 5
##        # def get_value(self):
####            return self.value +1
##class child(parent):
##    def get_value(self):
##        print(self.value + 1)
##        print(self.value - 1)
##    def func(self):
##        print(self.value * 5)
##
##
##
##
##c = child()
##c.get_value()
##c.func()


#method overriding(when there are two methods the first method is overrided and the second method is given the priority if it is in the child class
class parent():
    def __init__(self,value):
        self.value = value
    def get_value(self):
            return self.value +1
class child(parent):
    def get_value(self):
        print(self.value + 1)
        print(self.value - 1)
  




c = child(10)
c.get_value()

