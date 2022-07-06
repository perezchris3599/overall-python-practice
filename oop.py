#classes and objects in oop
#class Robot {
#    String name;
#    String color;
#    int weight;

    #adding constructor/function
#    Robot(String n, String c, int w) {
#        this.name = n;
#        this.color = c;
#        this.weight = w;
#    }
#}

#defining the class
class Robot:
#adding constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        print("My color is " + self.color)

#create an object
#r1 = Robot()
#r1.name = "Tom"
#r1.color = "red"
#r1.weight = 30

#created object 2
#r2 = Robot()
#r2.name = "Jerry"
#r2.color = "blue"
#r2.weight = 40

#no need to specify attribute names
#both object one and two summarized
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()
