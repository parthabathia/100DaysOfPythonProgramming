from tkinter import *

FONT = ("arial", 10)


def mile_to_km(*args):
    calculated_km_label.config(text=f"{int(miles_input.get()) * 1.61: 0.2f}")


window = Tk()
window.title("Miles to Km converter")
window.config(padx=30, pady=30)

miles_input = Entry()
miles_input.grid(column=1, row=0)
miles_input.focus()
miles_input.config(justify="center")
miles_input.bind("<Return>", mile_to_km)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(pady=10, padx=10)

equals_label = Label(text="is equal to", font=FONT)
equals_label.grid(column=0, row=1)
equals_label.config(pady=10, padx=10)

calculated_km_label = Label(text="0", font=FONT)
calculated_km_label.grid(column=1, row=1)
calculated_km_label.config(pady=10, padx=10)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(pady=10, padx=10)

calculate = Button(text="Calculate", command=mile_to_km, font=FONT)
calculate.grid(column=1, row=2)
calculate.config(padx=10, pady=10)

window.mainloop()