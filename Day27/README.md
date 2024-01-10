# Day 27 of Python programming bootcamp

The provided Python code is a simple graphical user interface (GUI) application using the Tkinter library for converting miles to kilometers. The program creates a window with an entry field to input the distance in miles, a "Calculate" button to perform the conversion, and labels to display the input, output, and conversion units.

Here's a breakdown of the code:

1. **Importing Tkinter:**
   ```python
   from tkinter import *
   ```
   Imports the Tkinter library, which is used to create the GUI.

2. **Setting Constants:**
   ```python
   FONT = ("arial", 10)
   ```
   Defines a constant font style for the GUI elements.

3. **Conversion Function:**
   ```python
   def mile_to_km(*args):
       calculated_km_label.config(text=f"{int(miles_input.get()) * 1.61: 0.2f}")
   ```
   Defines a function (`mile_to_km`) that performs the conversion when called. It takes the value entered in the miles entry field, multiplies it by 1.61 to convert to kilometers, and updates the text of the label (`calculated_km_label`) with the result.

4. **Creating the Main Window:**
   ```python
   window = Tk()
   window.title("Miles to Km converter")
   window.config(padx=30, pady=30)
   ```
   Creates the main window with a title and adds some padding.

5. **Input Entry Field:**
   ```python
   miles_input = Entry()
   miles_input.grid(column=1, row=0)
   miles_input.focus()
   miles_input.config(justify="center")
   miles_input.bind("<Return>", mile_to_km)
   ```
   Creates an entry field for inputting miles. The `justify` property centers the text, and the `bind` method associates the "Return" key with the `mile_to_km` function.

6. **Labels:**
   ```python
   miles_label = Label(text="Miles", font=FONT)
   equals_label = Label(text="is equal to", font=FONT)
   calculated_km_label = Label(text="0", font=FONT)
   km_label = Label(text="Km", font=FONT)
   ```
   Creates labels for "Miles," "is equal to," the calculated result, and "Km" respectively. These labels are placed in specific rows and columns using the `grid` method.

7. **Calculate Button:**
   ```python
   calculate = Button(text="Calculate", command=mile_to_km, font=FONT)
   calculate.grid(column=1, row=2)
   calculate.config(padx=10, pady=10)
   ```
   Creates a button labeled "Calculate" that, when clicked, calls the `mile_to_km` function. It is also placed in a specific row and column using the `grid` method.

8. **Main Loop:**
   ```python
   window.mainloop()
   ```
   Starts the Tkinter event loop, allowing the GUI to respond to user interactions.

When the user enters a distance in miles and presses "Enter" or clicks the "Calculate" button, the program converts the miles to kilometers and displays the result in the GUI.