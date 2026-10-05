# Day 17: Question model
#
# The Question class models one question in the quiz.
#
# Each Question object stores:
# - text
# - answer
#
# The test object and print statement below are preserved
# because they were present in the original Day 17 file.
#
class Question: 
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
new_q = Question("sdfsdf", "False")
print(new_q.text)