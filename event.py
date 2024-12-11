from tkinter import *

window = Tk()
window.title("Event Hanler")
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)
    
window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe buttom was clicked !")
    
button = Button(text = "Click me!")
button.pack()

button.bind("<Button>", handle_click)

window.mainloop()

    