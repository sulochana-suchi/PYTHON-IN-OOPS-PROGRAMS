# Area of circle using oops
import math
class circle:
    def_init_(self,r):
        self.r=r

        def calarea(self):
            return math.pi * self.r**2
        def cirper(self):
            return 2*math.pi * self.r

        #driver code
        r= float(input("Input the radius of the circle: "))
        a = circle(r)

        area = a.cirper()
        print("perimeter of the circle:",area)
