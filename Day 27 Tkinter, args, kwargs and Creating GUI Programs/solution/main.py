import tkinter


def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)


# Create Window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=350)
window.config(padx=20, pady=20)

# Create Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# Make the label visible on the Window
# my_label.pack(side="left")
# my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# my_label.pack()

# Button
button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)
# button.pack()

button2 = tkinter.Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=20)
input.grid(column=3, row=2)
# input.pack()

# Loop to keep the Window on the screen
window.mainloop()
