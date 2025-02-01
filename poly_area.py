class shape:
    def area(self):
        print("Area")
    
class rectange(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print(self.length*self.width)

class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        print(self.side*self.side)

a=rectange(4,5)
b=square(5)

for x in (a,b):
    x.area()

