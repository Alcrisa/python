import tkinter
import random
from turtle import*
window=tkinter.Tk()
print("¿Cómo te ves?")
button_1=tkinter.Button(window,text="Quiero mi copo",width=80)
button_1.pack(padx=10,pady=10)
button_2=tkinter.Button(window,text="Prefiero dibujar yo",width=80)
button_2.pack(padx=10,pady=10)
button_3=tkinter.Button(window,text="Salir",width=80)
button_3.pack(padx=10,pady=10)
def onClick_1(event):
    colors=["white","yellow","orange","HotPink","red"]
    shape("turtle")
    speed(10)
    pensize(5)
    Screen().bgcolor("blue")
    def vshape():
        right(25)
        forward(50)
        backward(50)
        left(50)
        forward(50)
        backward(50)
        right(25)
    def snowflakearm():
        for x in range(0,4):
            forward(30)
            vshape()
        backward(120)
    def snowflake():
        for y in range(0,12):
            color(random.choice(colors))
            snowflakearm()
            right(30)
    snowflake()
def onClick_2(event):
    import tkinter
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
def onClick_3(event):
    exit(window)
button_1.bind("<ButtonRelease>",onClick_1)
button_2.bind("<ButtonRelease>",onClick_2)
button_3.bind("<ButtonRelease>",onClick_3)
window.mainloop()
