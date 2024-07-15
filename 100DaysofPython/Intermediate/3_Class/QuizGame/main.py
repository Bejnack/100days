"""_summary_
main loop
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


print(quiz.still_has_questions())

while quiz.still_has_questions():
    quiz.next_question()
    
print(f"""You've completed the quizz!
Your final score is {quiz.score}/{quiz.question_number}.""")
