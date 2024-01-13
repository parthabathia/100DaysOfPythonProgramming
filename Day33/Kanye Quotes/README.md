# Day33 of Python programming bootcamp

This Python script uses the Tkinter library to create a simple graphical user interface (GUI) that displays random quotes from Kanye West's API. Here's a breakdown of the code:

1. **Import Libraries:**
   - `from tkinter import *`: Imports all classes, functions, and constants from the Tkinter library, which is used for creating the GUI.
   - `import requests`: Imports the `requests` library, which is used to send HTTP requests to Kanye West's API.

2. **Define Function:**
   - `get_quote()`: This function sends a GET request to the "https://api.kanye.rest/" API, retrieves a quote in JSON format, and updates the text displayed on the canvas with the fetched Kanye West quote.

3. **Create GUI Window:**
   - `window = Tk()`: Creates the main window of the GUI.
   - `window.title("Kanye Says...")`: Sets the title of the window.
   - `window.config(padx=50, pady=50)`: Configures the padding (internal margin) of the window.

4. **Create Canvas:**
   - `canvas = Canvas(width=300, height=414)`: Creates a canvas widget with a specified width and height.
   - `background_img = PhotoImage(file="background.png")`: Loads an image file as a background image.
   - `canvas.create_image(150, 207, image=background_img)`: Places the background image on the canvas.
   - `quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")`: Initializes a text element on the canvas with a default quote text.
   - `canvas.grid(row=0, column=0)`: Places the canvas in the first row and column of the grid.

5. **Create Button:**
   - `kanye_img = PhotoImage(file="kanye.png")`: Loads an image file for the Kanye West button.
   - `kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)`: Creates a button with the Kanye West image, removes the highlight border, and assigns the `get_quote` function to be executed on button click.
   - `kanye_button.grid(row=1, column=0)`: Places the button in the second row and first column of the grid.

6. **Start GUI Event Loop:**
   - `window.mainloop()`: Initiates the Tkinter event loop, allowing the GUI to respond to user interactions.

When the user clicks the Kanye West button, the `get_quote` function is triggered, fetching a random Kanye West quote from the API and updating the displayed text on the canvas. The background image and layout provide a visually appealing interface for the quote display.