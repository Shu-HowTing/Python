#Class
import turtle

def Draw_square(some_turtle):
    for i in range(2):
        some_turtle.forward(200) #等价于X.fd(100)
        some_turtle.right(150)
        some_turtle.forward(200)
        some_turtle.right(30)
def Draw_art():
    pass

    # X = turtle.Turtle()
    # X.shape("circle")
    # X.color("yellow")
    # X.speed(5)
    # for i in range (36):
    #     Draw_square(X)
    #     X.right(10)
    # X = turtle.Turtle()
    # X.shape("circle")
    # X.color("yellow")
    # X.speed(5)
    # X.right(90)
    # for i in range(36):
    #     Draw_square(X)
    #     X.right(10)


    #window.exitonclick()

# def Draw_circle():
#
#     Y = turtle.Turtle()
#     Y.shape("circle")
#     Y.color("yellow")
#     Y.circle(100)

# window = turtle.Screen()
# window.bgcolor("green")
# Draw_art()
# window.exitonclick()


#类的继承
class Parent():
    def __init__(self, last_name ='', eye_color =''  ):
        print("The parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last_name:",self.last_name)
        print("Eye_color:",self.eye_color)

class Child(Parent): #子类继承父类
    def __init__(self, last_name, eye_color, num_toys):
        print("The child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.num_toys = num_toys
    def show_info(self):
        print("Last_name:",self.last_name)
        print("Eye_color:",self.eye_color)
        print("Num_toys:", self.num_toys)


L_parent = Parent()
L_parent.show_info()
D_parent = Parent("Ding", "black")
D_child = Child("Ding", "black", 5)
#print(D_parent.eye_color)
#print(D_child.last_name)
#D_parent.show_info()
D_child.show_info()
















