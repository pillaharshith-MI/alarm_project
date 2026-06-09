import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.grid(row=0, column=0, columnspan=6)
colour = "red"
brush = 10


def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - brush, y - brush, x + brush, y + brush, fill=colour, outline=colour)


def set_brush(new_size):
    global brush
    brush = int(new_size)


def set_colour(c):
    global colour
    colour = c


size_slider = tk.Scale(root, from_=1, to=30, orient=tk.HORIZONTAL, label="Brush size", command=set_brush)
size_slider.grid(row=1, column=0)
red_btn=tk.Button(root, text="Red", command=lambda: set_colour("red"),fg="red")
red_btn.grid(row=1, column=1)
blue_btn = tk.Button(root, text="Blue", command=lambda: set_colour("blue"),fg="blue")
blue_btn.grid(row=1, column=2)
green_btn = tk.Button(root, text="Green", command=lambda: set_colour("green"),fg="green")
green_btn.grid(row=1, column=3)
erase_btn = tk.Button(root, text="Erase", command=lambda: set_colour("white"))
erase_btn.grid(row=1, column=4)
delete_btn = tk.Button(root, text="Delete", command=lambda: canvas.delete("all"))
delete_btn.grid(row=1, column=5)

canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-1>", draw)
root.mainloop()