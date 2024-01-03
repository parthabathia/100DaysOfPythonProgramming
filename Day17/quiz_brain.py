class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q{self.question_number + 1}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong Answer!")
        print(f"The correct answer was {self.question_list[self.question_number].answer}.")
        print(f"Your score is {self.score}/{self.question_number + 1}")
        self.question_number += 1
        print("\n")