from tkinter import Canvas, Tk
import time

# Constants for canvas and object sizes
CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400
CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas, eraser):
    """ Erase objects in contact with the eraser """
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    # Define eraser boundaries
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find overlapping objects and erase them
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    root = Tk()
    root.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
    canvas.pack()

    # Create grid of blue cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
    canvas.bind("<Button-1>", lambda event: canvas.create_rectangle(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill='pink'))
    root.mainloop()

    canvas.wait_for_click()  # Wait for user click before creating eraser
    last_click_x, last_click_y = canvas.get_last_click()

    # Create eraser
    eraser = canvas.create_rectangle(last_click_x, last_click_y, last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE, 'pink')

    # Move eraser and erase objects
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        time.sleep(0.05)

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
