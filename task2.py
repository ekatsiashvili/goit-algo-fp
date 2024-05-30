import turtle
import math

def draw_tree(branch_length, angle, depth):
    if depth == 0:
        return

    # Draw the main branch
    turtle.forward(branch_length)

    # Draw the left subtree
    turtle.left(angle)
    draw_tree(branch_length * 0.7, angle, depth - 1)

    # Draw the right subtree
    turtle.right(2 * angle)
    draw_tree(branch_length * 0.7, angle, depth - 1)

    # Return to the original position and orientation
    turtle.left(angle)
    turtle.backward(branch_length)

def main():
    # Set up the turtle environment
    turtle.speed('fastest')  # Set the turtle speed to the fastest
    turtle.left(90)  # Start drawing the tree pointing upwards
    turtle.up()  # Lift the pen up to move to the starting position
    turtle.backward(200)  # Move the turtle to the starting position
    turtle.down()  # Put the pen down to start drawing

    # Set the initial parameters
    branch_length = 100
    angle = 45
    depth = 9  # You can change the depth to any desired level of recursion

    # Draw the tree
    draw_tree(branch_length, angle, depth)

    # Finish the drawing
    turtle.done()

if __name__ == '__main__':
    main()