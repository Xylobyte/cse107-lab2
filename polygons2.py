import turtle

sides = int(input("Please enter the number of sides: "))
if(sides < 3):
    print("Error; the given number of sides is not valid. Please enter a value of at least 3.")
    exit(1)

length = float(input("Please enter the side-length: "))
if(length <= 0):
    print("Error; the given side-length is not valid. Please enter a value larger than 0.")
    exit(1)

window = turtle.Screen()
t1 = turtle.Turtle()
for i  in range(sides):
    t1.forward(length)
    t1.left(360 / sides)
window.mainloop()