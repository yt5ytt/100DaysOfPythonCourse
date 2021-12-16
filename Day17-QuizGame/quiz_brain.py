class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        num_of_questions = len(self.question_list)
        return self.question_number < num_of_questions

    def next_question(self):
        question = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        next_answer = input(f"Q.{self.question_number}: {question} (True/False)?: ")
        self.check_answer(next_answer, answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're right")
            self.score += 1
        else:
            print("You're wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}. \n")
