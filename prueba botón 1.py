import tkinter
window=tkinter.Tk()
print("¿Cómo te ves?")
button_1=tkinter.Button(window,text="Eres bobo",width=80)
button_1.pack(padx=10,pady=10)
button_2=tkinter.Button(window,text="No eres bobo",width=80)
button_2.pack(padx=10,pady=10)
button_3=tkinter.Button(window,text="No contesto",width=80)
button_3.pack(padx=10,pady=10)
def onClick_1(event):
    print("Lo sabía")
def onClick_2(event):
    print("No te lo crees ni tú")
def onClick_3(event):
    exit(window)
button_1.bind("<ButtonRelease>",onClick_1)
button_2.bind("<ButtonRelease>",onClick_2)
button_3.bind("<ButtonRelease>",onClick_3)
window.mainloop()


        
