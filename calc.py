import turtle
import random
import time

def draw_expression(a, b, y, result):
    expression = f"{a} {y} {b} = {result}"
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.clear()

    # Set text color to a random color using Turtle's built-in color names
    color_name = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
    turtle.color(color_name)

    # Draw the expression using the turtle
    turtle.write(expression, align="center", font=("Arial", 16, "normal"))

while True:
    a = input("Enter number 1 (or 'exit' to end): ")

    if a.lower() == 'exit':
        print("Exiting the calculator.")
        turtle.bye()
        break

    b = input("Enter number 2: ")
    y = input("Enter operation (+, -, *, /): ")

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if y == '+':
        result = a + b
    elif y == '-':
        result = a - b
    elif y == '*':
        result = a * b
    elif y == '/':
        if b == 0:
            print("Error: Division by zero.")
            continue
        result = a / b
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
        continue

    print("Calculating the output...")
    time.sleep(2)  # Simulate calculation time

    print(f"Opening the live turtle window....")
    time.sleep(1)  
    draw_expression(a, b, y, result)
    turtle.done()

