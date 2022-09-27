# fibonacci sequence using
import turtle
# Fibonacci Sequence !

# Importing the relevant modules
import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

# Create a Function

def Fibonacci(N):
    # Starting sequence
    starting_sequence = [1,1]

    #Our sequence will be as long as our 'N' value
    for i in range(2, N):
        for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(10)
    #Calculating the next number in the sequence
        next_number = starting_sequence[-1] + starting_sequence[-2]
    #Append this new number to our sequence
        starting_sequence.append(next_number)

    return starting_sequence

print(Fibonacci(10))
turtle.hideturtle()
#Plotting fibonacci numbers on a simple graph

# plt.plot(Fibonacci(10))
# plt.show()






















# def fiboPlot(n):
#     a = 0
#     b = 1
#     sqr_a = a
#     sqr_b = b
#
#     # Setting the color of the plotting pen to orange
#     y.pencolor("orange")
#
#     # Drawing the first sqr
#     y.forward(b * fac)
#     y.left(90)
#     y.forward(b * fac)
#     y.left(90)
#     y.forward(b * fac)
#     y.left(90)
#     y.forward(b * fac)
#
#     # Proceeding in the Fibonacci Series
#     temp = sqr_b
#     sqr_b = sqr_b + sqr_a
#     sqr_a = temp
#
#     # Drawing the rest of the sqrs
#     for i in range(1, n):
#         y.backward(sqr_a * fac)
#         y.right(90)
#         y.forward(sqr_b * fac)
#         y.left(90)
#         y.forward(sqr_b * fac)
#         y.left(90)
#         y.forward(sqr_b * fac)
#
#         # Proceeding in the Fibonacci Series
#         temp = sqr_b
#         sqr_b = sqr_b + sqr_a
#         sqr_a = temp
#
#     # Bringing the pen to starting point of the spiral plot
#     y.penup()
#     y.setposition(fac, 0)
#     y.seth(0)
#     y.pendown()
#
#     # Set the color of the plotting pen to red
#     y.pencolor("red")
#
#     # Fibonacci Spiral Plot
#     y.left(90)
#     for i in range(n):
#         print(b)
#         fdwd = math.pi * b * fac / 2
#         fdwd /= 90
#         for j in range(90):
#             y.forward(fdwd)
#             y.left(1)
#         temp = a
#         a = b
#         b = temp + b
#
#
# fac = 5
#
# m = int(input('Enter the no. of iterations (must be > 1): '))
#
# if m > 0:
#     print("Fibonacci series for", m, "elements :")
#     y = turtle.Turtle()
#     y.speed(100)
#     fiboPlot(m)
#     turtle.done()
# else:
#     print("No. of iterations must be > 0")
