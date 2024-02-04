from tkinter import *


def button_clicked():
    miles = user_input.get()
    km = int(miles) * 1.609
    answer_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
# miles_label.config(padx=20, pady=20)

# equal label
equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)
# equal_label.config(padx=20, pady=20)

# answer label
answer_label = Label(text=0, font=("Arial", 12, "bold"))
answer_label.grid(column=1, row=1)
# answer_label.config(padx=20, pady=20)

# km label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)
# km_label.config(padx=20, pady=20)

# Calculate Button
calculate_button = Button(text="Calculate", font=("Arial", 12, "bold"), command=button_clicked)
calculate_button.grid(column=1, row=2)
window.mainloop()
