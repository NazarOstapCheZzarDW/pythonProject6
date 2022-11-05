class Grandparents:
    height = 180
    age = 60
    sick = "koronovirus"

class Parents(Grandparents):
    age = 40
class Children(Parents):
    height = 170

    def init(self):
        print (self.sick)
        print(self.age)
        print(self.height)
daun = Children()
class Wow:
    def __wow(self):
        print ("Wooow")
    def _hello(self):
        print ("Hi!")
some_obj = Wow()
some_obj._hello()
some_obj.__wow()