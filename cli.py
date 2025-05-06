from shapes import Rectangle, Square
from canvas import Canvas

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))
canvas_color = input("Enter canvas color(white/black): ")
if canvas_color.lower() == 'white':
    canvas_color = (255, 255, 255)
elif canvas_color.lower() == 'black':
    canvas_color = (0, 0, 0)
else:
    print("Invalid or not implemented color. Please run the program again.", file=sys.stderr)

canvas = Canvas(canvas_height, canvas_width, canvas_color)

while True:
    shape_type = input("What would you like to draw? (square/rectangle) "
                       "Or type 'd' to stop the program and draw the result.")

    if shape_type.lower() == 'square':
        x_sq = int(input("Enter x for the placement of the square: "))
        y_sq = int(input("Enter y for the placement of the square: "))
        red_sq = int(input("Enter Red: "))
        green_sq = int(input("Enter Green: "))
        blue_sq = int(input("Enter Blue: "))
        color_sq = (red_sq, green_sq, blue_sq)
        side_sq = int(input("Enter a side length"))
        sq1 = Square(x=x_sq, y=y_sq,side=side_sq, color=color_sq)
        sq1.draw(canvas)
    if shape_type.lower() == 'rectangle':
        x_rect = int(input("Enter x for the placement of the rectangle: "))
        y_rect = int(input("Enter y for the placement of the rectangle: "))
        red_rect = int(input("Enter Red: "))
        green_rect = int(input("Enter Green: "))
        blue_rect = int(input("Enter Blue: "))
        color_rect = (red_rect, green_rect, blue_rect)
        height_rect = int(input("Enter height for rectangle: "))
        width_rect = int(input("Enter width for rectangle: "))
        rect1 = Rectangle(x=x_rect, y=y_rect, height=height_rect,width=width_rect, color=color_rect)
        rect1.draw(canvas)
    if shape_type == 'd':
        break

canvas.make("output.png")
