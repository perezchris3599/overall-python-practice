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
    def introduce_self(self):
        print("My name is " + self.name)

#create an object
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = "30"
r1.introduce_self()
