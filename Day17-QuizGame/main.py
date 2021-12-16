from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dict_name in question_data:
    text = dict_name["question"]
    answer = dict_name["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {brain.score}/{brain.question_number}")
