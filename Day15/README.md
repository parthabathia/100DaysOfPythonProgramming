# Day 15 of Python programming bootcamp

This Python code defines a simple coin-operated coffee machine simulation. The program allows users to select from three types of coffee (Espresso, Latte, Cappuccino), check the available resources, and turn off the machine. Users can insert coins, and if the payment is sufficient, the program dispenses the selected coffee and returns any change. The state of available resources and profit is also tracked.

Here's a breakdown of the key components in the code:

1. **`get_report` function:**
   - Displays the current availability of resources (milk, water, coffee) and the total money earned.

2. **`check_resources` function:**
   - Checks if there are enough resources to make the selected coffee.
   - Returns `True` if there are sufficient resources; otherwise, it prints an error message and returns `False`.

3. **`process_coins` function:**
   - Takes user input for the number of quarters, dimes, nickels, and pennies inserted.
   - Calculates the total amount inserted and returns it.

4. **`transaction_success` function:**
   - Checks if the money received is sufficient to cover the cost of the selected drink.
   - If successful, it calculates and prints the change, updates the profit, and returns `True`. Otherwise, it prints an error message and returns `False`.

5. **`make_drink` function:**
   - Deducts the required ingredients for the selected drink from the available resources.

6. **Main Program:**
   - Initializes the profit variable and sets the machine to operate.
   - Enters a loop where users can select a coffee type, check the report, or turn off the machine.
   - If a coffee is selected, it checks resources, processes coins, and completes the transaction if possible.

Note: The code uses a `MENU` dictionary to store information about each type of coffee (ingredients and cost) and a `resources` dictionary to store the current availability of ingredients. The global variable `profit` tracks the total money earned. The program runs until the user decides to turn off the machine.