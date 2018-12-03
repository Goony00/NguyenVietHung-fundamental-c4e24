from turtle import *

speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for index, colors in enumerate(colors):
    color(colors, colors)
    
    begin_fill()

    for i in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    forward(50)

    end_fill()



mainloop()