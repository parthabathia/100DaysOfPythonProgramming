# Day 17 of Python programming bootcamp

This Python code is a simple quiz application that utilizes a set of questions and answers. Here's a breakdown of the code:

1. **Importing Modules:**
   ```python
   from data import question_data
   from question_model import Question
   from quiz_brain import QuizBrain
   ```
   The code imports three modules: `question_data`, `Question` class from `question_model`, and `QuizBrain` class from `quiz_brain`.

2. **Creating a Question Bank:**
   ```python
   question_bank = [Question(item["question"], item["correct_answer"]) for item in question_data]
   ```
   The code generates a list called `question_bank` by iterating over the items in `question_data`. For each item, it creates a `Question` object using the question and correct answer information.

3. **Initializing QuizBrain:**
   ```python
   quiz = QuizBrain(question_bank)
   ```
   An instance of the `QuizBrain` class is created, passing the `question_bank` as a parameter to the constructor.

4. **Executing the Quiz:**
   ```python
   while quiz.still_has_question():
       quiz.next_question()
   ```
   The code runs a loop as long as there are still questions remaining in the quiz. Inside the loop, the `next_question` method of the `QuizBrain` instance is called, presenting the next question to the user.

5. **Displaying Results:**
   ```python
   print("You've completed the quiz!")
   print(f"Your final score was: {quiz.score}/{quiz.question_number}")
   ```
   Once the user has completed all the questions, a completion message is printed along with the user's final score, which is the number of correct answers out of the total number of questions.

In summary, this code defines a quiz application that reads questions and answers from an external data source, quizzes the user on those questions, and then displays the user's final score after completing the quiz. The actual logic for presenting questions, handling user input, and tracking the score is implemented in the `QuizBrain` class.