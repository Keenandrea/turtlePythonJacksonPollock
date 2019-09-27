"""
program: Paint Blobs

created on Thu Sep 26 20:37:39 2019

author: Keenan W. Andrea

course: CMP SCI 4500 Featuring Dr. Keith W. Miller

purpose: a program using Turtle graphics to sketch a grid in a graphics window
and subsequentially drop circles, colored at random, into random cells among th
e sketched grid. before the program finishes, stats about the program run, name
ly average, minimum, and maximum, are displayed in both console- and and Turtle
graphics-windows. Here is the warp and woof of program execution:

On the screen, ask the interactive user to enter an integer between 2 and 10 in
clusive. This will determine the size of your square grid. I will call this num
ber N. If the user enters something illegal, give an error message and keep ask
ing until you get something appropriate. Next, ask the interactive user to ente
r an integer between 1 and 10 inclusive. This will tell your program how many “
paintings” it will make. I will call this number K. If the user enters somethin
g illegal, give an error message and keep asking until you get something approp
riate. Make an N X N random paint blob painting K times. As each of the K paint
ings is being made, display graphics on the screen to show the interactive user
how the painting is proceeding. You have great latitude as to how you will disp
lay the painting as it fills up with paint. At the very least, the interactive 
user should be able to tell which cells have NO paint so far, which cells have 
SOME paint so far, which is implemented by a random color in given cell, and wh
ich cell is being painted right at the moment, which is implemented by the buil
t-in turtle image. This minimum would require three distinct colors. However, y
ou might be able to think of a clever way to visually communicate more informat
ion about the painting than no paint, some paint, and currently being painted. 
Be thoughtful and creative about this, please. Give some thought as to how quic
kly you want to paint drops to appear in your simulation. After a painting “fin
ishes,” alert the interactive user, and inform them that they must push ENTER (
or RETURN) to continue. After all K paintings have been finished (including the
final ENTER push by the user), display the following statistics from all the pa
intings: The minimum, maximum, and average number of paint blobs it took to pai
nt a picture; and the minimum, maximum, and average number that describes the m
ost paint blobs that fell into any one cell in a painting. 
    
data structures: lists are used in this program to hold the blobs dropped on an
y single painting for each painting and again to hold the most blobs dropped on
any single cell for each painting. these lists are emplyed to eke out the maxim
um in each list over all paintings painted. moreover, a 2-d array is used to ai
d in the labeling of coordinate (x, y) pairs so the programmer can intangibly v
isualize what cell, or, x,y coordinate the Turtle is currently acting upon. 

naming conventions: variables are instantiated using Pythonic snake_case. in ad
dition, the variables are named in artistic terms, for instance, instead of a g
rid, the 2-d array is called a canvas, and so on.
"""

#============================================================================#
# library imports. the bulk of this program leans on Turtle graphics, which i#
# uses Tkinter for underlying graphics. 
#============================================================================#
import turtle
import random

from turtle import Screen
from turtle import Turtle
#============================================================================#
#============================================================================#

#============================================================================#
# function prompts user for input with regards to the size of a grid that will
# be implemented during program execution. function guards against illegal use
# r input, and loops until user correctly chooses an Integer between two and f 
# ifteen for grid size, in keeping with program assignment requirements      #
#                                                                            #
# the second function performs the same logic as the first, guarding against t
# he same cases, except that the input will determine how many paintings the p
# rogram will produce.                                                       #
#============================================================================#
def get_grid_size(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        
        if value < 2 or value > 10:
            print("Sorry, input must neither be less than 2 nor ",end="")
            print("greater than 10. Please enter using a correct input.")
            continue
        else:
            break
        
    return value

def get_paintings(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        
        if value < 1 or value > 10:
            print("Sorry, input must neither be less than 1 nor ",end="")
            print("greater than 10. Please enter using a correct input.")
            continue
        else:
            break
        
    return value
#============================================================================#
#============================================================================#

#============================================================================#
# function commits to the same logic as the two above, except that user must #
# press the ENTER key to exit the instantiated loop.
#============================================================================#
def to_continue(prompt):    
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        
        if value == '':
            print("Instantiating blank canvas...Painting...\n")
            break
        else:
            print("Sorry, to continue enter a single return carriage ",end="")
            print("devoid of all alphanumerics and special characters aside.")
            print("Please press ENTER.")
            continue
#============================================================================#
#============================================================================#
    
#============================================================================#
# function sets up the grid, or canvas by first drawing equidistant lines alo#
# ng the y-coordinate according to the grid_size determined by program user, #
# then drawing equidistant lines along the x-coordinate according to the grid#
# _size determined by the user
#============================================================================#
def setup_canvas():
    pencil = Turtle(visible=False)
    pencil.speed('normal')

    pencil.penup()
    pencil.goto(-cell_size * grid_size / 2, cell_size * (grid_size / 2 - 1))

    for _ in range(grid_size - 1):
        pencil.pendown()
        pencil.forward(grid_size * cell_size)
        pencil.penup()
        pencil.goto(-cell_size * grid_size / 2, pencil.ycor() - cell_size)

    pencil.goto(-cell_size * (grid_size / 2 - 1), cell_size * grid_size / 2)

    pencil.setheading(270)

    for _ in range(grid_size - 1):
        pencil.pendown()
        pencil.forward(grid_size * cell_size)
        pencil.penup()
        pencil.goto(pencil.xcor() + cell_size, cell_size * grid_size / 2)
    
    pencil.clear()
#============================================================================#
#============================================================================#
        
#============================================================================#
# function takes a neat little trick with Python string formatting and joinin#
# g to give the dots dripped on the canvas a different color everytime, chose#
# n by random hexidecimals generated by random number/character generator    #
#============================================================================#
def drip_color():
    # little trick to produce randomly colored paint drops with hexidecimals
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return color
#============================================================================#
#============================================================================#

        
#============================================================================#
#============================================================================#
def paint_canvas():
    # create a new turtle robot
    artist = Turtle(visible=False)

    painted = 0
    blobs = 0
    painted_over = 0
    most_drip_drops = 0 
    
    # instantiate the 2-d array
    canvas = [0] * grid_size
    for i in range(grid_size):
        canvas[i] = [0] * grid_size
  
    # set the coordinates
    # of our first paint
    # blob at the center 
    # of the canvas grid
    drip = grid_size // 2
    drop = grid_size // 2

    # turn the position of the rob
    # ot at the center of the grid
    drip, drop = artist.position()
    most_drip_drops = canvas[0][0]
    
    # while loop shuffles randomly through the
    # grid/canvas, leaping up from a random co
    # ordinate, then setting down into another
    # random coordinate. this logic is repeate
    # d until every cell has been painted upon
    while (painted < (grid_size * grid_size)):
        # set drip drop coordinates at random
        drip = random.randint(0, grid_size - 1)
        drop = random.randint(0, grid_size - 1)
        
        # set the turtle robot
        # as a stamp so user c
        # an visualize where t
        # he randomization wit
        # hin the grid is occu
        # ring
        artist.color("#000000")
        artist.shape("turtle")
        brush = artist.stamp()
        
        artist.penup()
        artist.goto((drip - grid_size // 2) * cell_size, 
                    (drop - grid_size // 2) * cell_size)
        
        # if the cell has not been 
        # painted upon, and the dr
        # rip drop has selected it
        # we add the count of that
        # cell into the correct x,
        # y coordinates of our 2-d
        # array and fill the cell
        # with a randomized color
        if canvas[drip][drop] == 0:
           # uncomment the commented line below for testing
           # print("drip: {}, drop: {}".format(drip,drop))
           canvas[drip][drop] = 1
           
           # fills cell with a
           # random hexidecimal
           # value from function
           # drip_color
           color = drip_color()
           artist.begin_fill()
           artist.color(color)
           artist.circle(random.randint(10,20))
           artist.end_fill()
           painted += 1
        
        # if there already has be
        # en a drip drop, or rand
        # om traversal over the a
        # ctive cell, add one to
        # the active x,y coordina
        # te of the 2d array
        if canvas[drip][drop] > 0:
            canvas[drip][drop] += 1
            # update the x,y coordinate with the max
            # number of drip drops for later stats
            if canvas[drip][drop] > most_drip_drops:
                most_drip_drops = canvas[drip][drop]
            painted_over += 1
               
        # clear the turtle logo
        # stamp, which can be th
        # ought of as resetting 
        # the turtle logo stamp
        # to the new random cell
        artist.clearstamp(brush)
        blobs += 1
         
    # clear the turtle graphic, r
    # eturn the aggregate of blob
    # bs dropped on the canvas, o
    # r grid, and return the most 
    # drips dropped in one cell.         
    artist.clear()         
    return blobs, most_drip_drops  
#============================================================================#
#============================================================================#

#============================================================================#
#============================================================================#
print("What dimensions would you like your grid to have?")
grid_size = get_grid_size("Please enter a number between two and fifteen: ")
print("Thank you. Now: How many paintings do you wish to create?")
paintings = get_paintings("Please enter a number between one and ten: ")

# set the turtle
# graphics window
# to 600, 600 hei
# ght by width and
# give it a title
screen = Screen()
turtle.title ('Turtle Pollack')
screen.setup(600, 600)

cell_size = 32
p_blobs = 0
p_blobs_ttl = 0
p_blobs_max_lst = []
most_drips_dropped = []
most_drip_drop = 0

painting = 0
# while the number of pain
# tings fed into the progr
# am by user input, as spe
# cified in the assignment
# description has not yet 
# been reached by one + one
# increment, create another
# canvas, or grid, and paint
while painting < paintings:
    
    # function call
    # draws the grid
    setup_canvas()
    # function call places blobs at random
    p_blobs, most_drip_drop = paint_canvas()
    
    # there are two cases to this program,
    # the first case is one painting paint
    # ed, and the second case is multiple 
    # paintings painted from 2 - 10. if th
    # ere is only one painting painted, mo
    # st of the resetting of window and tu
    # rtle robots can be bypassed. that is
    # what the conditional below commits t
    # o doing, fit with proper console and 
    # graphics window output to guide the
    # user through the program execution
    if paintings > 1:
        turtle.color('Sea Green')
        turtle.write("Press ENTER",align="center",font=("Courier", 20, "normal"))
        turtle.hideturtle()     
        p_blobs_max_lst.append(p_blobs)
        most_drips_dropped.append(most_drip_drop)     
        p_blobs_ttl += p_blobs
        to_continue("Please press ENTER for a new canvas.")
        turtle.clear()
    # increment the paintings
    painting = painting + 1

# now we are out of the loop that builds
# a canvas, or grid, and paints paint bl
# obs onto the canvas at random. now we
# can gather statistics and diplay results
print("That wraps up your collection.") 
pen = Turtle(visible=True)
pen.color('Sea Green')
pen.write("Press ENTER to host your art exhibition",align="center",font=("Courier", 15, "normal")) 
pen.hideturtle()
to_continue("Press ENTER to take them to the gallery.")    
pen.clear()
#============================================================================#
#============================================================================#

#============================================================================#
# Printing out the statistics of our paint blobs in regards to the paintings.#
# if only one painting was made, the statistics are easily calculated in the #
# else conditional branch. the if branch calculates for multiple paintings pa#
# inted. stats are diplayed in console as well as turtle graphics screen     #
#============================================================================#
print("Paint Blobs Gallery\n===== ===== =======")
if paintings > 1:
    print("Average Blobs In Paintings: {}".format(p_blobs_ttl / paintings))
    print("Maximum Blobs In Paintings: {}".format(max(p_blobs_max_lst)))
    print("Minimum Blobs In Paintings: {}".format(min(p_blobs_max_lst)))
    
    print("Average Blobs In Cells: {}".format(round(max(most_drips_dropped) / paintings)))
    print("Maximum Blobs In Cell: {}".format(max(most_drips_dropped)))
    print("Minimum Blobs In Cell: 1")
    
    # same as before, there are two ways in which this program can be executed,
    # the first way is if the user calls for a single painting, and the second 
    # is if the user calls for any number of paintings between two and 10. the
    # statistics alter accordingly to each case, and what is printed in the con
    # sole window and Turtle graphics windows are changed between conditionals
    
    # the long lines of programming are those lines that print to the turtle gr
    # aphics window, and are long because many parameters must be passed in ord
    # er for them to the ran. future considerations may emply loops to shrinken
    # the code bloat.
    
    # from turtle graphics window output to output, or, write to write, the pen
    # object must be moved to a new coordiante along the window, otherwise the
    # write is instantiated on the same line and the readability is egregious.
    pen.color('Sea Green')
    pen.write("Paint Blobs Gallery\n===== ===== =======",align="center",font=("Courier", 20, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write(("\n\nAverage Blobs In Paintings: {}".format(round(p_blobs_ttl / paintings))),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write(("\n\nMaximum Blobs In Paintings: {}".format(max(p_blobs_max_lst))),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write(("\n\nMinimum Blobs In Paintings: {}".format(min(p_blobs_max_lst))),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    
    pen.write(("\nAverage Blobs In Cells: {}".format(round(sum(most_drips_dropped) / paintings))),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write(("\n\nMaximum Blobs In Cell: {}".format(max(most_drips_dropped))),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write("\n\nMinimum Blobs In Cell: 1",align="center",font=("Courier", 12, "normal"))
    pen.hideturtle()
else:
    print("Average Blobs In Paintings: {}".format(p_blobs))
    print("Maximum Blobs In Paintings: {}".format(p_blobs))
    print("Minimum Blobs In Paintings: {}".format(p_blobs))
    
    print("Average Blobs In Cells: {}".format(p_blobs))
    print("Maximum Blobs In Cell: {}".format(most_drip_drop))
    print("Minimum Blobs In Cell: 1")
    
    pen.color('Sea Green')
    pen.write("Paint Blobs Gallery\n===== ===== =======",align="center",font=("Courier", 20, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write("Average Blobs In Paintings: {}".format(p_blobs),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write("\nMaximum Blobs In Paintings: {}".format(p_blobs),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write("\nMinimum Blobs In Paintings: {}".format(p_blobs),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    
    pen.write("\nAverage Blobs In Cells: {}".format(p_blobs),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write("\nMaximum Blobs In Cell: {}".format(most_drip_drop),align="center",font=("Courier", 12, "normal"))
    pen.penup()
    pen.forward(grid_size * cell_size)
    pen.goto(-cell_size * grid_size / 2, pen.ycor() - cell_size)
    pen.pendown()
    pen.write("\nMinimum Blobs In Cell: 1",align="center",font=("Courier", 12, "normal"))
    pen.hideturtle()

# last statement
screen.mainloop()
# shut down turtlegr
# aphics on a click
turtle.done()
#============================================================================#
#============================================================================#