# Day 17: Quiz Project
# Final project main file
#
# This file keeps the original Day 17 project logic.
#
# Responsibilities:
# - Import the Question class
# - Import the question data
# - Import the QuizBrain class
# - Convert each question dictionary into a Question object
# - Store all Question objects in question_bank
# - Create the QuizBrain object
# - Run the quiz until there are no questions left
# - Print the final score
#
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")