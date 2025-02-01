class subject:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    
class tamil(subject):
    def study(self):
        print("Tamil study")
    
class english(subject):
    def study(self):
        print("English study")

class maths(subject):
    def study(self):
        print("Maths study")

class science(subject):
    def study(self):
        print("science study")
    
class social(subject):
    def study(self):
        print("social study")

tam=tamil("Tamil",85)
eng=english("Engilsh",74)
math=maths("Maths",67)
sci=science("Science",58)
soc=social("Social",95)

for x in(tam,eng,math,sci,soc):
    print(x.name)
    print(x.mark)
    x.study()