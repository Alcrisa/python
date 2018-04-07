import tkinter
print("Bienvenido al programa de dibujo de Alberto: Alberdraw")
print("Para dibujar mantenga pulsado el botón izquierdo del ratón y muevaló")
print("Para cambiar de pincel haga click en el color deseado")
window=tkinter.Tk()
canvas=tkinter.Canvas(window, width=750, height=500, bg="yellow")
canvas.pack()
lastX, lastY=0,0
color="blue"
def store_position(event):
    global lastX, lastY
    lastX=event.x
    lastY=event.y
def on_click(event):
    store_position(event)
def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=color, width=4)
    store_position(event)
canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
red_id=canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id=canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id=canvas.create_rectangle(10, 60, 30, 80, fill="black")
green_id=canvas.create_rectangle(10, 85, 30, 105, fill="green")
yellow_id=canvas.create_rectangle(10, 110, 30, 130, fill="yellow")
def set_color_red(event):
    global color
    color="red"
def set_color_blue(event):
    global color
    color="blue"
def set_color_black(event):
    global color
    color="black"
def set_color_green(event):
    global color
    color="green"
def set_color_yellow(event):
    global color
    color="yellow"
canvas.tag_bind(red_id, "<Button-1>", set_color_red)
canvas.tag_bind(blue_id, "<Button-1>", set_color_blue)
canvas.tag_bind(black_id, "<Button-1>", set_color_black)
canvas.tag_bind(green_id, "<Button-1>", set_color_green)
canvas.tag_bind(yellow_id, "<Button-1>", set_color_yellow)
window.mainloop()



