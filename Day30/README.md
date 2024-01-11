# Day 30 of Python programming bootcamp

This Python script utilizes the Tkinter library to create a graphical user interface (GUI) for a simple password manager application. The program allows users to store, retrieve, and generate passwords for various websites. Here's a breakdown of the key functionalities:

1. **Password Generator Functionality:**
   - The `generate_password` function creates a random password consisting of letters (both uppercase and lowercase), numbers, and symbols.
   - The generated password is displayed in the UI and copied to the clipboard using the `pyperclip` module.

2. **Search Details Functionality:**
   - The `search_details` function retrieves stored login information (email and password) for a specific website.
   - It reads data from a JSON file named "password_manager.json" and displays the details if the website is found; otherwise, it shows an error message.

3. **Save Password Functionality:**
   - The `save` function stores website, email, and password information in the "password_manager.json" file.
   - If the file does not exist, it creates a new one; otherwise, it updates the existing data.

4. **User Interface (UI) Setup:**
   - The Tkinter `Tk` class is used to create the main window for the application.
   - The UI includes entry fields for website, email, and password, along with buttons for searching, generating passwords, and saving data.
   - An image ("logo.png") is displayed at the top using the Tkinter `Canvas` widget.

5. **Initialization:**
   - The script initializes the Tkinter window, sets its title to "Password Manager," and configures padding.
   - Entry fields are pre-filled with default or placeholder values for better user guidance.

6. **Buttons:**
   - The "Search" button triggers the `search_details` function.
   - The "Generate Password" button triggers the `generate_password` function.
   - The "Add" button triggers the `save` function to store the provided details.

7. **Error Handling:**
   - The program handles potential errors, such as missing data or a missing data file, and displays appropriate error messages using Tkinter's `messagebox`.

8. **Security Considerations:**
   - While this script provides basic password management functionality, it's important to note that storing sensitive information in a local file may not be the most secure method. In a production environment, it's recommended to use secure storage mechanisms and encryption.

Note: The script assumes the existence of a logo image ("logo.png") in the same directory. Ensure that the required image file is available for proper execution.