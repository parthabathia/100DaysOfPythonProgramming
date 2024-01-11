# Day 29 of Python programming bootcamp

**Description: Password Manager GUI with Tkinter**

The provided code is a Python script that creates a graphical user interface (GUI) for a simple password manager application using the Tkinter library. This application allows users to generate random passwords and save website login details securely.

**Key Features:**

1. **Password Generator:**
   - The "Generate Password" button triggers the `generate_password` function, creating a random password consisting of letters (both lowercase and uppercase), numbers, and symbols.
   - The generated password is displayed in the "Password" entry widget and is also copied to the clipboard using the `pyperclip` library.

2. **Save Password:**
   - The user can input website details, including the website name, username/email, and password.
   - The "Add" button triggers the `save` function, which confirms the entered details through a messagebox and, if confirmed, appends the details to a text file named "password_manager.txt".
   - The text file is formatted with each entry in the form of "Website | Username | Password".

3. **User Interface (UI):**
   - The UI includes entry fields for the website name, username/email, and password.
   - A "Generate Password" button allows users to create secure passwords.
   - The company logo is displayed using a canvas.
   - The "Add" button saves the entered details.

4. **Default Values:**
   - The username_entry has a default value ("abc@xyz.com") pre-inserted for convenience.

5. **File Handling:**
   - The script uses file I/O to store the login details in a text file ("password_manager.txt").
   - Existing details are appended to the file, ensuring that previous entries are not overwritten.

6. **Error Handling:**
   - A messagebox is used to notify users if essential details (website name or password) are missing when attempting to save.

**Usage:**
   - Users can run the script to open the GUI.
   - They can generate passwords and save website login details.

**Note:**
   - The logo.png file is expected to be present in the same directory as the script for the logo to be displayed.

This code provides a basic foundation for a password manager application and can be further enhanced with additional features such as encryption, password strength evaluation, and the ability to retrieve stored passwords.