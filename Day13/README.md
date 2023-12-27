# Day 13 of Python programming bootcamp

The provided code is a collection of Python snippets with intentional bugs, and it is meant to serve as a debugging exercise. Each section of the code has a specific problem that needs to be identified and corrected. Here's a description for each part:

1. **Describe Problem:**
   - The `my_function` is intended to print "You got it" when the loop reaches 20, but there's a bug. The loop runs from 1 to 19, so it will never reach 20.

2. **Reproduce the Bug:**
   - Generates a random number between 1 and 6 to index `dice_imgs` list. However, the list is zero-indexed, so it should be `randint(0, 5)` instead of `randint(1, 6)`.

3. **Play Computer:**
   - Asks for the user's year of birth and tries to categorize them as a millennial or Gen Z. There's no handling for the case when the user's birth year is exactly 1994. It would be more accurate to use `<= 1994` instead of `< 1994` in the second condition.

4. **Fix the Errors:**
   - Asks for the user's age and attempts to print a message if the age is over 18. However, the input is treated as a string, and there's a missing indentation for the `print` statement. The age should be converted to an integer using `int(age)`.

5. **Print is Your Friend:**
   - Asks for the number of pages and words per page to calculate the total number of words. However, there's a typo in `word_per_page == int(input("Number of words per page: "))`, where `==` should be replaced with `=` to assign the value to `word_per_page`.

6. **Use a Debugger:**
   - Defines a function `mutate` that is intended to create a new list (`b_list`) by doubling each element in the input list (`a_list`). However, the `append` statement is outside the loop, so it only appends the last doubled item. It should be indented to be inside the loop.

After addressing these issues, the code will run correctly and fulfill its intended functionality.