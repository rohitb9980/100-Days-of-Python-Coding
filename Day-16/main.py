# from turtle import Turtle, Screen
#
# rohit = Turtle()
# print(rohit)
# rohit.shape("turtle")
# rohit.color("red")
# rohit.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)